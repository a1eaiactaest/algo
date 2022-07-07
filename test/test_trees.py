#!/usr/bin/env python3

from ads.trees import BinaryTree, array2bintree

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

  def remove_on_one_node(self):
    root = BinaryTree(10)
    self.assertEqual(repr(root), 'BinaryTree(data=10, right=None, left=None)')
    root.remove(10)
    self.assertEqual(repr(root), 'BinaryTree(data=None, right=None, left=None)')


if __name__ == "__main__":
  unittest.main()

    
