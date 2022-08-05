from typing import List
def rec_fibn(n: int) -> int:
  """Return n-th element of fibonacci sequence using recursion.
  It's zero-indexed, so 

  n: x
  0: 1
  1: 1
  2: 2
  3: 3
  4: 5
  ...

  """
  if n < 2:
    return 1
  return rec_fibn(n-2) + rec_fibn(n-1)

def memo_fibn(n: int) -> int:
  """Return n-th element of the fibonacci sequence using memoization."""
  mem = [0,1,1,2]

  if n < 2:
    return mem[n]
  
  for _ in range(3,n):
    mem.append(mem[len(mem)-1] + mem[len(mem)-2])

  return mem[n]

if __name__ == "__main__":
  i = 0
  while (1):
    print(i, memo_fibn(i))
    i += 1
