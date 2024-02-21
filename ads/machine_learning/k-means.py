#!/usr/bin/env python3

"""
Reference: https://en.wikipedia.org/wiki/K-means_clustering
"""

import math
import matplotlib.pyplot as plt
import numpy as np


Scalar = int | float
Vector = tuple[Scalar, Scalar]


def md_pythagorean(*args: Vector):
  acc = 0
  for arg in args:
    x, y = arg
    acc += (x - y)**2
  return math.sqrt(acc)



if __name__ == "__main__":
  nums = [(3,4), (4,4), (4,5), (1,1), (4,5)]
  print(md_pythagorean(*nums))

    
    

  
