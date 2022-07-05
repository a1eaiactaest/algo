#!/usr/bin/env python3

import unittest

from ads.parsing import postfix
from ads.parsing import valid_parentheses

class TestPosFix(unittest.TestCase):
  def test_spaces(self):
    equation_string = "3 5 * 4 +"
    self.assertEqual(postfix(equation_string), 19.0) 
    del equation_string

  def test_no_spaces(self):
    equation_string = "35*4+" # in case of joined numbers postif splits them. it's 3 and 5 not 35.
    self.assertEqual(postfix(equation_string), 19.0) 
    del equation_string

  def test_complex_no_spaces(self):
    equation_string = "23-4+567*+*"
    self.assertEqual(postfix(equation_string), 141.0) 
    del equation_string

  def test_complex_spaces(self):
    equation_string = "2 3 - 4 + 5 6 7 * + *"
    self.assertEqual(postfix(equation_string), 141.0) 
    del equation_string

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
