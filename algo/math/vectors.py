from typing import Tuple, Union, List

def dot(a: List, b: List) -> Union[int, float]:
  assert len(a) == len(b), "vectors must be the same size."
  acc = 0
  for ai,bi in zip(a,b):
    acc += ai*bi
  return acc

if __name__ == "__main__":
  print(dot([1,3,-5],[4,-2,-1]))
  print(dot([5,-2,1],[3,7,3]))
  print(dot([2,5,6],[3,4,-5]))
  print(dot([1,4,-2], [5,3,-2]))