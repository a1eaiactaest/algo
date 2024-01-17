#!/usr/bin/env python3

class Hanoi:
  def __init__(self, n: int):
    self.n = n
    self.A = [_ for _ in range(self.n, 0, -1)]
    self.B = []
    self.C = []
    self.moves = 0
    print(list(self))

  def __iter__(self):
    for t in [self.A, self.B, self.C]:
      yield t

  def move(self, n: int, src: list, tmp: list, dst: list) -> None:
    if n > 0:
      self.move(n-1, src, dst, tmp)
      dst.append(src.pop())
      self.moves += 1
      print(self.moves, list(self))
      self.move(n-1, tmp, src, dst)

  def solve(self):
    self.move(self.n, self.A, self.B, self.C)
    return self.moves

if __name__ == "__main__":
  N = 10
  H = Hanoi(N)
  ret = H.solve()
  print('Total moves:', ret)
  assert (2**N)-1 == ret, 'wrong number of moves'
