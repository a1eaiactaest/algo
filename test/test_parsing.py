#!/usr/bin/env python3

import unittest

from ads.parsing import valid_parentheses

class TestVlidParetheses(unittest.TestCase):
  def test_round(self):
    case1 = '(())'
    case2 = '()'
    case3 = '('

    self.assertTrue(valid_parentheses(case1))
    self.assertTrue(valid_parentheses(case2))
    self.assertFalse(valid_parentheses(case3))
    del case1, case2, case3
  
  def test_square(self):
    pass
    case1 = '[]'
    case2 = '[][][[][]]'
    case3 = '[[[]'

    self.assertTrue(valid_parentheses(case1))
    self.assertTrue(valid_parentheses(case2))
    self.assertFalse(valid_parentheses(case3))
    del case1, case2, case3

  def test_curly(self):
    pass
    case1 = '{}{}'
    case2 = '{{{}{}}}{}'
    case3 = '{{}{{}'

    self.assertTrue(valid_parentheses(case1))
    self.assertTrue(valid_parentheses(case2))
    self.assertFalse(valid_parentheses(case3))
    del case1, case2, case3

if __name__ == '__main__':
  unittest.main()
