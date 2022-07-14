#!/usr/bin/env python3

from ads.trees import BinaryTree 
from .utils import pprint_default

import unittest

class TestBinaryTree(unittest.TestCase):
  def test_instance_empty_tree(self):
    root = BinaryTree()
    self.assertEqual(type(root), BinaryTree)
    del root

  def test_instance_tree(self):
    root = BinaryTree(1337)
    self.assertEqual(type(root), BinaryTree)
    del root

  def test_repr_empty(self):
    root = BinaryTree()
    self.assertEqual(repr(root), 'BinaryTree(data=None, right=None, left=None)')
    del root

  def test_repr(self):
    root = BinaryTree(1337)
    self.assertEqual(repr(root), 'BinaryTree(data=1337, right=None, left=None)')
    del root

  def test_insert(self):
    root = BinaryTree(10)
    self.assertEqual(repr(root), 'BinaryTree(data=10, right=None, left=None)')
    root.insert(11)
    self.assertEqual(repr(root), 'BinaryTree(data=10, right=BinaryTree(data=11, right=None, left=None), left=None)')
    root.insert(9)
    self.assertEqual(repr(root), 'BinaryTree(data=10, right=BinaryTree(data=11, right=None, left=None), left=BinaryTree(data=9, right=None, left=None))')
    del root

  def test_insert_on_empty(self):
    root = BinaryTree()
    root.insert(10)
    self.assertEqual(repr(root), 'BinaryTree(data=10, right=None, left=None)')
    del root

  def test_remove_on_one_node(self):
    root = BinaryTree(10)
    self.assertEqual(repr(root), 'BinaryTree(data=10, right=None, left=None)')
    root.remove(10)
    self.assertEqual(repr(root), 'BinaryTree(data=None, right=None, left=None)')

  def test_size(self):
    root = BinaryTree(10)
    root.insert(11)
    root.insert(12)
    root.insert(15)
    self.assertEqual(root.size, 4)

  def test_size_one_node(self):
    root = BinaryTree(10)
    self.assertEqual(root.size, 1)

  def test_size_empty(self):
    root = BinaryTree()
    self.assertEqual(root.size, 0)

  def test_height(self):
    root = BinaryTree()
    self.assertEqual(root.height, 0)

  def test_height_two(self):
    root = BinaryTree(12)
    root.right = BinaryTree(10)
    self.assertEqual(root.height, 1)

  def test_leaves_empty(self):
    root = BinaryTree()
    self.assertEqual(root.leaves, [])

  def test_leaves(self):
    root = BinaryTree(10)
    self.assertEqual(root.leaves, [10])

  def test_leaves_two(self):
    root = BinaryTree(10)
    root.left = BinaryTree(11)
    root.right = BinaryTree(12)
    root.right.right = BinaryTree(13)
    self.assertEqual(root.leaves, [11,13])


class TestBinaryTreeUtils(unittest.TestCase):
  def test_pretty_print(self):
    lines = pprint_default([10])
    self.assertEqual(lines, ['-(10)'])
    lines = pprint_default([35,28,31,59,23,55,67,50,56,30])
    self.assertEqual(lines, [
      '      ┌─-(67)', 
      '  ┌─-(59)', 
      '  │   │   ┌─-(56)', 
      '  │   └─-(55)', 
      '  │       └─-(50)', 
      '-(35)', 
      '  │   ┌─-(31)', 
      '  │   │   └─-(30)', 
      '  └─-(28)', 
      '      └─-(23)'])

if __name__ == "__main__":
  unittest.main()

