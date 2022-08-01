import matplotlib.pyplot as plt
import numpy as np
import math

def trick(n):
  """Sum of series of integers from 0 up to :n:
  Also known as Gauss Summation or Gauss Trick
  
  n = 10
  1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = ?
  (1 + 10) + (2 + 9) + (3 + 8) + (4 + 7) + (5 + 6) = ?
  (11) + (11) + (11) + (11) + (11) = ?
  which is equal to: (10 * (11)) // 2
  """
  return (n * (n + 1)) // 2

def distribution(x, mu=0, sigma=1):
  z = 1./sigma * math.sqrt(2*math.pi)
  return z*pow(math.e, -(x-mu)**2/(2*sigma*sigma))

def plot_distribution():
  X = np.arange(-5, 5, .1)
  Y1 = list(map(lambda x: distribution(x), X))
  Y2 = list(map(lambda x: distribution(x, 2, 1), X))
  plt.plot(X, Y1)
  plt.bar(X, Y1)
  plt.show()


if __name__ == "__main__":
  print(trick(100))
  plot_distribution()