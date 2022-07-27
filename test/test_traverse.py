#!/usr/bin/env python3

from ads.structures import BinaryTree, build_binary_tree
from ads.traversal import dfs_binary, bfs_binary, binary_search

import unittest

test_tree = build_binary_tree([35,28,31,59,23,55,67,50,56,30])
empty = BinaryTree()

class TestTraversal(unittest.TestCase):
  def test_dfs_binary(self):
    self.assertEqual(dfs_binary(test_tree), [35, 28, 23, 31, 30, 59, 55, 50, 56, 67])

  def test_bfs_binary(self):
    self.assertEqual(bfs_binary(test_tree), [35, 28, 59, 23, 31, 55, 67, 30, 50, 56])

  def test_dfs_binary_only_root(self):
    self.assertEqual(dfs_binary(BinaryTree(10)), [10])

  def test_bfs_binary_only_root(self):
    self.assertEqual(bfs_binary(BinaryTree(10)), [10])

  def test_dfs_binary_empty(self):
    self.assertEqual(dfs_binary(empty), [])
  
  def test_bfs_binary_empty(self):
    self.assertEqual(bfs_binary(empty), [])
    
class TestSearch(unittest.TestCase):
  def test_binarysearch(self):
    example_array = [35,28,31,59,23,55,67,50,56,30]
    self.assertEqual(binary_search(example_array, 23), 4)

  def test_binarysearch_two(self):
    example_array = [_ for _ in range(-100, 100)]
    self.assertEqual(binary_search(example_array, 0), 100)
  
  def test_binarysearch_non_existant(self):
    example_array = [35,28,31,59,23,55,67,50,56,30]
    self.assertEqual(binary_search(example_array, 1337), -1)

  def test_binarysearch_empty(self):
    example_array = []
    self.assertEqual(binary_search(example_array, 1337), -1)

  def test_binarysearch_big_set(self):
    example_array = [_ for _ in range(1000000)]
    self.assertEqual(binary_search(example_array, 1337), 1337)

if __name__ == "__main__":
  unittest.main()
