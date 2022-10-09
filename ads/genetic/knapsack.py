#!/usr/bin/env python3

from typing import List
import random

'''
0-1 Knapsack problem.

Reference: https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem

box:
  - value
  - weight 


there are N boxes, which can be represented as following:
  >>> class Box:
  >>>   def __init__(self, value, weight):
  >>>     self.value = value
  >>>     self.weight = weight

there's a weight limit for our knapsack, let's say 10 weights.
having boxes: Box(5, 2), Box(1, 7), Box(3, 1), Box(9, 10)
we can only pick those which sum of weights isn't bigger than the limit.
the point is to gather as much value with as little weight.
'''


class Box:
  def __init__(self, value, weight):
    self.value = value
    self.weight = weight

  def __repr__(self):
    return f"Box(v={self.value}, w={self.weight})"

def generate_boxes(n: int) -> List[List["Box"]]:
  '''Generate N boxes
  '''
  boxes: List["Box"] = []
  for _ in range(n):
    value = random.randint(0, 100)
    weight = random.randint(0, 100)
    boxes.append(Box(value, weight))
  return boxes

class KnapsackProblem:
  def __init__(self):
    self.boxes = generate_boxes(10)

if __name__ == "__main__":
  k = KnapsackProblem()
  print(k.boxes)
