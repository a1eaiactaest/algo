import unittest

from binary_search import *
from binary_tree_traversals import *

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)

class TestBinarySearch(unittest.TestCase):
  def test_case(self):
    arr = [_ for _ in range(100)]
    self.assertEqual(binary_search(arr, 1), 1)
    self.assertEqual(binary_search(arr, 99), 99)
    self.assertEqual(binary_search(arr, 0), 0)
    self.assertEqual(binary_search(arr, 101), None)
    self.assertEqual(binary_search(arr, -1), None)

  def test_empty(self):
    self.assertEqual(binary_search([], 1), None)

class TestBinaryTreeTraversals(unittest.TestCase):
  def test_inorder(self):
    self.assertEqual(inorder(root), [5, 2, 1, 3])

  def test_preorder(self):
    self.assertEqual(preorder(root), [1, 2, 5, 3])

  def test_postorder(self):
    self.assertEqual(postorder(root), [5, 2, 3, 1])

print(root)