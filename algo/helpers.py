import os
import sys
import time
import pstats
import hashlib
import pathlib
import cProfile
import tempfile
import platform
import functools
import contextlib
import numpy as np
import urllib.request
from tqdm import tqdm 
from io import StringIO
from typing import Optional, List, Callable

PLAT = platform.system()
assert PLAT == 'Darwin' or PLAT == 'Linux', f"Unsupported platform: {PLAT}"
CACHE_DIR = os.path.expanduser('~/Library/Caches') if PLAT == 'Darwin' else os.path.expanduser('~/.cache')

def sequential(l1:List[Callable]): return functools.reduce(lambda x,f: f(x), l1)

def colored(st:str, color:Optional[str], background=False):
  if color is not None:
    return f"\u001b[{10*background+60*(color.upper() == color)+30+['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'].index(color.lower())}m{st}\u001b[0m"
  else: return st

def timeit(function):
  def wrap(*args, **kwargs):
    start_time = time.time()
    ret = function(*args, **kwargs)
    end_time = time.time()
    execution_time = (end_time-start_time)

    # Round to one microsecond (1s/1000000)
    print("Execution time of %s was %2.6fs."%(function, execution_time))
    return ret
  return wrap

def _format_fcn(fcn): return f'{fcn[0]}:{fcn[1]}:{fcn[2]}'
class Profiling(contextlib.ContextDecorator):
  def __init__(self, enabled=True, sort='cumtime', frac=0.2, fn=None, ts=1):
    self.enabled = enabled
    self.sort = sort
    self.frac = frac
    self.fn = fn
    self.time_scale = 1e3/ts
  def __enter__(self):
    self.pr = cProfile.Profile()
    if self.enabled: self.pr.enable()
  def __exit__(self, *exc):
    if self.enabled:
      self.pr.disable()
      if self.fn: self.pr.dump_stats(self.fn)
      stats = pstats.Stats(self.pr).strip_dirs().sort_stats(self.sort)
      for fcn in stats.fcn_list[0:int(len(stats.fcn_list)*self.frac)]:
        (_, num_calls, tottime, cumtime, callers) = stats.stats[fcn]
        scallers = sorted(callers.items(), key=lambda x: -x[1][2])
        print(f"n:{num_calls:8d}  tm:{tottime*self.time_scale:7.2f}ms  tot:{cumtime*self.time_scale:7.2f}ms",
              colored(_format_fcn(fcn), "yellow") + " "*(50-len(_format_fcn(fcn))),
              colored(f"<- {(scallers[0][1][2]/tottime)*100:3.0f}% {_format_fcn(scallers[0][0])}", "BLACK") if len(scallers) else '')

class Timing(contextlib.ContextDecorator):
  def __init__(self, prefix='', on_exit=None, enabled=True):
    self.prefix = prefix
    self.on_exit = on_exit
    self.enabled = enabled
  def __enter__(self): self.st = time.perf_counter_ns()
  def __exit__(self, *exc):
    et = time.perf_counter_ns()
    self.t = et - self.st
    if self.enabled:
      print(f'{self.prefix}{self.t*1e-6:6.2} ms'+(self.on_exit(self.t) if self.on_exit else ''))

class MeasureFLOPS(contextlib.ContextDecorator):
  ups = {
    'M': 1e-6,
    'G': 1e-9,
    'T': 1e-12,
    'P': 1e-15,
  }
  def __init__(self, Nflop:int, unit_prefix='G', prefix='', on_exit=None, enabled=True):
    self.Nflop = Nflop
    self.unit_prefix = unit_prefix
    self.prefix = prefix
    self.on_exit = on_exit
    self.enabled = enabled
  def __enter__(self): self.st = time.monotonic()
  def __exit__(self, *exc):
    et = time.monotonic()
    self.t = et - self.st
    flops = self.Nflop/self.t
    if self.enabled:
      print(f'{self.prefix} {(flops*self.ups[self.unit_prefix]):.2f} {self.unit_prefix}FLOPS, {self.t*1e3:.2f} ms'+(self.on_exit(self.t) if self.on_exit else ''))
        
class CaptureOutput(list[str]):
  def __enter__(self) -> "CaptureOutput":
    self._original_stdout = sys.stdout
    self._temp_stdout = StringIO()
    sys.stdout = self._temp_stdout
    return self

  def __exit__(self, *args) -> None:
    lines = self._temp_stdout.getvalue().splitlines()
    self.extend(line.rstrip() for line in lines)
    sys.stdout = self._original_stdout


@functools.lru_cache(maxsize=None)
def getenv(key:str, default=0): return type(default)(os.getenv(key, default))

def fetch(url: str, name: Optional[str]=None, allow_cache=(not getenv('DISABLE_HTTP_CACHE'))):
  if url.startswith(('/', '.')): return pathlib.Path(url)
  fp = None
  if name is not None and (isinstance(name, pathlib.Path) or '/' in name):
    fp = pathlib.Path(name)
  else:
    if name: fn = name
    else: fn = hashlib.md5(url.encode('utf-8')).hexdigest()
    fp = pathlib.Path(CACHE_DIR)/'algo'/'downloads'/fn
    print(f'fetching from a cached file at {fp}')
  if not fp.is_file() or not allow_cache:
    with urllib.request.urlopen(url, timeout=10) as r:
      assert r.status == 200
      total_bytes = int(r.headers.get('Content-Length', 0))
      progress_bar = tqdm(total=total_bytes, unit='B', unit_scale=True, desc=url)
      (path := fp.parent).mkdir(parents=True, exist_ok=True)
      with tempfile.NamedTemporaryFile(dir=path, delete=False) as f:
        print(f'saving from {r} to tmp file at {f}')
        while chunk := r.read(16384):
          progress_bar.update(f.write(chunk))
        f.close()
        if (file_size := os.stat(f.name).st_size) < total_bytes:
          raise RuntimeError(f'fetch incomplete, file size mismatch: {file_size} < {total_bytes}')
        pathlib.Path(f.name).rename(fp)
  return fp

def torch_load(fn:str, save:Optional[bool]=False, name:Optional[str]=None) -> tuple[str, dict]:
  import torch
  if not isinstance(fn, pathlib.Path): fn = pathlib.Path(fn)
  state = torch.load(fn)
  weights = {k: v.to(torch.float32).numpy() for k,v in state.items()}
  fn = name if name else fn.stem
  fp = pathlib.Path(CACHE_DIR)/'algo'/'weights'/fn/'weights.npz'
  fp.parent.mkdir(parents=True, exist_ok=True)
  np.savez(fp, **weights)
  return str(fp), weights