import time

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