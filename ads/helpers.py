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


