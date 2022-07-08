#!/usr/bin/env python3

from ads.trees import BinaryTree, array2bintree
from ads.traversal import dfs_binary, bfs_binary

import unittest

test_tree = array2bintree([35,28,31,59,23,55,67,50,56,30])

class TestTraversal(unittest.TestCase):
  def test_dfs_binary(self):
    self.assertEqual(dfs_binary(test_tree), [35, 28, 23, 31, 30, 59, 55, 50, 56, 67])

  def test_bfs_binary(self):
    self.assertEqual(bfs_binary(test_tree), [35, 28, 59, 23, 31, 55, 67, 30, 50, 56])

  def test_dfs_binary_empty(self):
    empty = BinaryTree()
    self.assertEqual(dfs_binary(empty), [])

if __name__ == "__main__":
  unittest.main()
