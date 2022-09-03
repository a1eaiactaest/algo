from typing import List, Union

def standard_deviation(sample:List[Union[int,float]]) -> float:
  mean = sum(sample)/len(sample)
  acc = 0
  for x in sample:
    acc += (x-mean)**2
  return (acc/len(sample))**0.5
