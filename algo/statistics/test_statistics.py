import unittest
import numpy as np
import scipy

import standard_deviation
import linear_regression

# accurate up to 12th decimal point
ROUND = 12

class TestStandardDeviation(unittest.TestCase):
  def test_case(self):
    self.assertEqual(standard_deviation.stdev([6,2,3,1]), 1.8708286933869707)
    self.assertEqual(standard_deviation.stdev(sorted([6,2,3,1])), 1.8708286933869707)

    self.assertEqual(standard_deviation.stdev([1,4,7,2,6]), 2.280350850198276)
    self.assertEqual(standard_deviation.stdev(sorted([1,4,7,2,6])), 2.280350850198276)

  def test_compare_numpy(self):
    for _ in range(100):
      sample_data = np.random.random_sample(100,)
      numpy_res = np.std(sample_data)
      my_res = standard_deviation.stdev(sample_data)
      self.assertEqual(round(numpy_res, ROUND), round(my_res, ROUND)) # round to 5th decimal point
  
  def test_small(self):
    for x in range(100):
      self.assertEqual(standard_deviation.stdev([x]), .0)
      self.assertEqual(standard_deviation.stdev([x, x+1]), .5)
      self.assertEqual(standard_deviation.stdev([x, x+1, x+2]), 0.816496580927726)
      self.assertEqual(standard_deviation.stdev([x, x+1, x+2, x+3]), 1.118033988749895)

  def test_mixed_arrays(self):
    arr = [6,2,3,1]
    self.assertEqual(standard_deviation.stdev(arr), standard_deviation.stdev(sorted(arr)))
    arr = np.random.uniform(-1, 0, 1000)
    self.assertEqual(round(standard_deviation.stdev(arr), ROUND), round(standard_deviation.stdev(sorted(arr)), ROUND))

  def test_cmp_numpy(self):
    for _ in range(100):
      sample_data = np.random.uniform(-1, 0, 1000)
      numpy_res = np.std(sample_data)
      my_res = standard_deviation.stdev(sample_data)
      self.assertEqual(round(numpy_res, ROUND), round(my_res, ROUND))

class TestLinearRegression(unittest.TestCase):
  def test_example(self):
    X = range(1,8)
    Y = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]
    l = linear_regression.least_squares(X,Y)
    slope = l.slope
    y_int = l.y_intercept
    self.assertEqual(round(slope, 9), 2.414285714)
    self.assertEqual(round(y_int, 9), -0.828571429)

  def test_cmp_scipy(self):
    X = range(1,8)
    Y = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]

    l = linear_regression.least_squares(X,Y)
    slope = l.slope
    y_int = l.y_intercept

    res_scipy = scipy.stats.linregress(X,Y)
    res_slope = res_scipy.slope
    res_yint = res_scipy.intercept

    self.assertEqual(round(slope, ROUND), round(res_slope, ROUND))
    self.assertEqual(round(y_int, ROUND), round(res_yint, ROUND))

  def test_cmp_scipy_no_y(self):
    Y = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]

    with self.assertRaises(TypeError):
      l = linear_regression.least_squares(Y)

  def test_random(self):
    for i in range(10, 1000):
      X = range(i)
      Y = np.random.uniform(-100, 100, i)

      l = linear_regression.least_squares(X,Y)
      slope = l.slope
      y_int = l.y_intercept

      res_scipy = scipy.stats.linregress(X,Y)
      res_slope = res_scipy.slope
      res_yint = res_scipy.intercept

      self.assertEqual(round(slope, ROUND-5), round(res_slope, ROUND-5))
      self.assertEqual(round(y_int, ROUND-5), round(res_yint, ROUND-5))

if __name__ == "__main__":
  unittest.main()
