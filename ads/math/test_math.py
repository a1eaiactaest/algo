import unittest
import numpy as np

import gauss
import vectors
import matrix
import collatz
import find_max
import exponentation as exp


ROUND = 5

class TestGauss(unittest.TestCase):
  def test_trick(self):
    self.assertEqual(gauss.trick(100), 5050)
    self.assertEqual(gauss.trick(1), 1)
    self.assertEqual(gauss.trick(0), 0)
    self.assertEqual(gauss.trick(-1), 0)

  def test_normal_distribution(self):
    self.assertEqual(round(gauss.distribution(1)), round(0.2419707))

class TestVectors(unittest.TestCase):
  def test_dot(self):
    self.assertEqual(vectors.dot([1,4,-2], [5,3,-2]), 21)
    self.assertEqual(vectors.dot([1],[1]), 1)
    
    with self.assertRaises(AssertionError):
      print(vectors.dot([1,2,3], [1,2,3,4]))

class TestMatrix(unittest.TestCase):
  def test_constructor(self):
    M = matrix.Matrix([[1,2],[3,4]])
    self.assertIsInstance(M, matrix.Matrix)

    with self.assertRaises(TypeError):
      M = matrix.Matrix([[1,2],[3,4,5]])

    with self.assertRaises(TypeError):
      M = matrix.Matrix([1,2,3])

  def test_comparison_operators(self):
    A = matrix.Matrix([[1,2,3], [4,5,6], [7,8,9]])
    B = matrix.Matrix([[1,2,3], [4,5,6]])
    self.assertTrue(A > B)
    self.assertFalse(A < B)
    self.assertTrue(A != B)

  def test_mul(self):
    A = matrix.Matrix([[1,4,-2], 
                       [3,5,-6]])
    B = matrix.Matrix([[5,2,8,-1], 
                       [3,6,4,5], 
                       [-2,9,7,-3]])
    AB = matrix.Matrix([[21,8,10,25],
                        [42,-18,2,40]])

    self.assertTrue(A*B == AB)

    A = matrix.Matrix([[2,2],[2,2]])
    B = matrix.Matrix([[2,2],[2,2]])
    AB = matrix.Matrix([[8,8],[8,8]])

    self.assertTrue(A*B == AB)
  
  def test_identitiy(self):
    AB = matrix.Matrix([[8,8],[8,8]])
    ABi = matrix.Matrix([[1,0],[0,1]])
    self.assertEqual(AB.identity(), ABi)

# TODO: fib tests

class TestCollatz(unittest.TestCase):
  def test_case(self):
    self.assertEqual(collatz.collatz(4), (3, [4,2,1]))
    self.assertEqual(collatz.collatz(11), (15, [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]))
    self.assertEqual(collatz.collatz(31), (
      107,
      [
        31,
        94,
        47,
        142,
        71,
        214,
        107,
        322,
        161,
        484,
        242,
        121,
        364,
        182,
        91,
        274,
        137,
        412,
        206,
        103,
        310,
        155,
        466,
        233,
        700,
        350,
        175,
        526,
        263,
        790,
        395,
        1186,
        593,
        1780,
        890,
        445,
        1336,
        668,
        334,
        167,
        502,
        251,
        754,
        377,
        1132,
        566,
        283,
        850,
        425,
        1276,
        638,
        319,
        958,
        479,
        1438,
        719,
        2158,
        1079,
        3238,
        1619,
        4858,
        2429,
        7288,
        3644,
        1822,
        911,
        2734,
        1367,
        4102,
        2051,
        6154,
        3077,
        9232,
        4616,
        2308,
        1154,
        577,
        1732,
        866,
        433,
        1300,
        650,
        325,
        976,
        488,
        244,
        122,
        61,
        184,
        92,
        46,
        23,
        70,
        35,
        106,
        53,
        160,
        80,
        40,
        20,
        10,
        5,
        16,
        8,
        4,
        2,
        1,
        ])
    )

class TestMinMax(unittest.TestCase):
  def test_max(self):
    sample = np.random.random_sample(100)
    self.assertEqual(find_max.find_max(sample), max(sample))

  def test_max_recursive(self):
    sample = np.random.random_sample(100)
    self.assertEqual(find_max.find_max_r(sample, 0, len(sample)-1), max(sample))

  def test_max_recursive_against_iterative(self):
    sample = np.random.random_sample(100)
    self.assertEqual(find_max.find_max_r(sample, 0, len(sample)-1), find_max.find_max(sample))


class TestExponentation(unittest.TestCase):
  def test_case(self):
    out_set = [(2.0, 10, 1024.0), (2.1, 3, 9.261), (2.0,  -2, 0.25)]
    for s in out_set:
      base = s[0]
      e = s[1]
      self.assertEqual(exp.exp(base, e), pow(base, e))
      self.assertEqual(exp.exp_r(base, e), pow(base, e))
      self.assertEqual(exp.exp_r(base, e), exp.exp(base, e))
