#!/usr/bin/env python3

from typing import List
import random

'''
0-1 Knapsack problem.

Reference: https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
http://www.sc.ehu.es/ccwbayes/docencia/kzmm/files/AG-knapsack.pdf

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
  def __init__(self, value: int, weight: int) -> None:
    self.value = value
    self.weight = weight
  
  @property
  def vtw_ratio(self) -> float:
    return self.value/self.weight

  def __repr__(self) -> str:
    return f"Box(v={self.value}, w={self.weight})"

def generate_boxes(n: int, max_weight: int) -> List[List["Box"]]:
  '''Generate N boxes
  '''
  boxes: List["Box"] = []
  for _ in range(n):
    value = random.randint(0, max_weight)
    weight = random.randint(0, max_weight)
    boxes.append(Box(value, weight))
  return boxes

class KnapsackProblem:
  def __init__(self) -> None:
    self.weight_limit = 200
    self.boxes = generate_boxes(10, self.weight_limit-100)
    self.sort_boxes()
    for box in self.boxes:
      print(box, box.vtw_ratio)

  def sort_boxes(self) -> None:
    '''Sort boxes in place by value/weight ratio in non-increasing order.

    Fitness function:
    "GAs require a fitness function which allocates a score to each chromosome in the current
    population. Thus, it can calculate how well the solutions are coded and how well they
    solve the problem [2]."

    '''
    self.boxes.sort(key=lambda box: box.value/box.weight, reverse=True)

  # TODO: finish implementing main loop
  def run(self) -> None:
    generations = 250
    for g in range(generations):
      raise NotImplementedError

if __name__ == "__main__":
  k = KnapsackProblem()
  print(k.boxes)
