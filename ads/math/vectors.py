from typing import Tuple, Union

def dot(a: Tuple, b: Tuple) -> Union[int, float]:
  assert len(a) == len(b), "vectors must be the same size."
  acc = 0
  for ai,bi in zip(a,b):
    acc += ai*bi
  return acc

if __name__ == "__main__":
  print(dot((1,3,-5),(4,-2,-1)))