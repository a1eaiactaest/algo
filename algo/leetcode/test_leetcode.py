import unittest 

import shuffle

class TestLeetcode(unittest.TestCase):
  def test_shuffle(self):
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    self.assertEqual(shuffle.shuffle(nums, n), [1,4,2,3,3,2,4,1])
