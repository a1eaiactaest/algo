from typing import List, Tuple
def collatz(x: int) -> Tuple[int, List[int]]:
  assert isinstance(x, int), 'must be int'

  p = [x]
  while x != 1:
    if x % 2 == 0:
      x //= 2
    else:
       x = (3*x) + 1
    p.append(x)
  return len(p), p

if __name__ == "__main__":
  print(collatz(31))
  print(collatz(4))
