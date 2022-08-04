import unittest
import numpy as np

import gauss
import vectors
import matrix

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