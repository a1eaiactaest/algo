import unittest

import ints
import parentheses
import postfix

class TestInts(unittest.TestCase):
  def test_case(self):
    self.assertEqual(ints.ints("i have 1 dog and 2 cats."), [1,2])
    self.assertEqual(ints.ints("my favorite number is 1337, not one thousand three hundred thirty seven"), [1337])
    self.assertEqual(ints.ints("he33llo 42 I'm a 32 string 30"), [30,32,33,42])

class TestParentheses(unittest.TestCase):
  def test_validate(self):
    self.assertTrue(parentheses.valid('[][][][[]]'))
    self.assertTrue(parentheses.valid('([])(){}'))
    self.assertTrue(parentheses.valid('()((([])))[{([])}]'))
    self.assertFalse(parentheses.valid(')('))

class TestPostfix(unittest.TestCase):
  def test_calculator(self):
    self.assertEqual(postfix.eval('3 3 +'), 6.0)
    self.assertEqual(postfix.eval('6 9 + 6 9 * +'), 69.0) # hehe



