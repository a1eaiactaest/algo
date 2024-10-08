#!/usr/bin/env python3

import numpy as np


class HopfieldNetwork:
  def __init__(self, n_neurons: int) -> None:
    self.n_neurons = n_neurons
    self.weights = np.zeros((n_neurons, n_neurons))

  def train(self, patterns:np.ndarray) -> None:
    for pattern in patterns:
      pattern = pattern.reshape(-1, 1)
      self.weights += pattern @ pattern.T
    np.fill_diagonal(self.weights, 0)


  def recall(self, pattern:np.ndarray, max_iterations:int=100) -> np.ndarray:
    pattern = pattern.copy()
    for _ in range(max_iterations):
      for i in range(self.n_neurons):
        activation = np.dot(self.weights[i], pattern)
        pattern[i] = np.sign(activation)
    return pattern


# binary to bipolar
def bipolarize(pattern):
  return np.where(pattern == 0, -1, 1)

if __name__ == "__main__":
  N = 1000
  H = HopfieldNetwork(N)

  patterns = np.array([[1, 0, 1, 0], [0, 1, 0, 1]])
  patterns = np.array([bipolarize(p) for p in patterns])

  H.train(patterns)

  # noisy version of patterns[0]
  test_pattern = np.array([1, 0, 1, 1]) 
  bipolar_test_pattern = bipolarize(test_pattern)
  print(f"test pattern (noisy): {test_pattern}")
  recalled_pattern = H.recall(bipolar_test_pattern)
  binary_recalled_pattern = np.where(recalled_pattern == -1, 0, 1)
  print(f"recalled pattern: {binary_recalled_pattern}")

