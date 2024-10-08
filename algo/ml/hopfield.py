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

# generates already polarized
def gen_rand_patterns(n_patterns, n_neurons):
  return np.random.choice([-1, 1], size=(n_patterns, n_neurons))

if __name__ == "__main__":
  np.random.seed(50058)

  n_neurons = 100
  H = HopfieldNetwork(n_neurons)

  n_patterns = 5
  patterns = gen_rand_patterns(n_patterns, n_neurons)
  print(patterns)
  #patterns = np.array([bipolarize(p) for p in patterns])

  H.train(patterns)

  test_pattern_idx = 0
  original_pattern = patterns[test_pattern_idx]

  noisy_pattern = original_pattern.copy()
  noise_indices = np.random.choice(n_neurons, size=int(.1*n_neurons), replace=False)
  print(noise_indices)
  noisy_pattern[noisy_pattern] *= -1 # apply noise by flipping selected bits

  print(f"originl pattern: {original_pattern}")
  print(f"noisy pattern: {noisy_pattern}")

  recalled_pattern = H.recall(noisy_pattern)

  print(f"recalled pattern: {recalled_pattern}")

  acc = np.mean(recalled_pattern == original_pattern)
  print(f"acc of recall {acc}")

