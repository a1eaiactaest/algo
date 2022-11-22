import unittest

from hanoi import Hanoi

class TestHanoi(unittest.TestCase):
  def test_case(self):
    for i in range(10):
      H = Hanoi(i)
      ret = H.solve()
      self.assertEqual(ret, (2**i)-1)

