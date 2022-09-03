import unittest
import numpy as np

import standard_deviation

class TestStandardDeviation(unittest.TestCase):
  def test_case(self):
    self.assertEqual(standard_deviation.standard_deviation([6,2,3,1]), 1.8708286933869707)
    self.assertEqual(standard_deviation.standard_deviation(sorted([6,2,3,1])), 1.8708286933869707)

    self.assertEqual(standard_deviation.standard_deviation([1,4,7,2,6]), 2.280350850198276)
    self.assertEqual(standard_deviation.standard_deviation(sorted([1,4,7,2,6])), 2.280350850198276)

  def test_compare_numpy(self):
    for _ in range(100):
      sample_data = np.random.random_sample(100,)
      numpy_res = np.std(sample_data)
      my_res = standard_deviation.standard_deviation(sample_data)
      self.assertEqual(round(numpy_res, 5), round(my_res, 5)) # round to 5th decimal point

if __name__ == "__main__":
  unittest.main()