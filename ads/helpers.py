import time
import contextlib

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
        

