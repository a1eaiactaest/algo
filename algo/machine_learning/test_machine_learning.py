import unittest
import numpy as np

from losses import *

class TestLosses(unittest.TestCase):
  def test_mse(self):
    true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    predicted_values = np.array([1.2, 1.9, 2.8, 4.2, 5.1, 5.9])
    self.assertAlmostEqual(mean_squared_error(true_values, predicted_values), 0.024, places=1)
  
  def test_mse_dl(self): # different lengths
    true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    predicted_values = np.array([1.9, 2.8, 4.2, 5.1])
    with self.assertRaises(ValueError):
      mean_squared_error(true_values, predicted_values)
  
  def test_mae(self):
    true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    predicted_values = np.array([1.2, 1.9, 2.8, 4.2, 5.1, 5.9])
    self.assertAlmostEqual(mean_absolute_error(true_values, predicted_values), 0.2)