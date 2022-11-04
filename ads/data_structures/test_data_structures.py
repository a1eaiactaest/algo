import unittest
import random
import sys

try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO


import binary_tree as bt
from linked_list import *

class CaptureOutput(list[str]):
  """Catch stdout."""

  def __enter__(self) -> "CaptureOutput":
    self._original_stdout = sys.stdout
    self._temp_stdout = StringIO()
    sys.stdout = self._temp_stdout
    return self

  def __exit__(self, *args: Any) -> None:
    lines = self._temp_stdout.getvalue().splitlines()
    self.extend(line.rstrip() for line in lines)
    sys.stdout = self._original_stdout

def pprint_linked_list(linked_list) -> str:
  with CaptureOutput() as output:
    linked_list.pretty()
  return ''.join([line for line in output if line != ""])

class TestBinaryTree(unittest.TestCase):
  def test_instance_empty_tree(self):
    n = bt.Node(1337)
    root = bt.BinaryTree(n)
    self.assertEqual(type(root), bt.BinaryTree)
    del root, n

  def test_instance_tree(self):
    n = bt.Node(1337)
    root = bt.BinaryTree(n)
    self.assertEqual(type(root), bt.BinaryTree)
    del root

  def test_instance_tree_with_int(self):
    root = bt.BinaryTree(1337)
    self.assertEqual(type(root), bt.BinaryTree)
    del root

  def test_repr_empty(self):
    root = bt.BinaryTree()
    self.assertEqual(repr(root), 'BinaryTree(None)')
    del root

  def test_repr(self):
    root = bt.BinaryTree(1337)
    self.assertEqual(repr(root), "BinaryTree({'1337': (None, None)})")
    del root

  def test_insert(self):
    root = bt.BinaryTree(10)
    self.assertEqual(repr(root), "BinaryTree({'10': (None, None)})")
    root.insert(11)
    self.assertEqual(repr(root), "BinaryTree({'10': (None, {'11': (None, None)})})")
    root.insert(9)
    self.assertEqual(repr(root), "BinaryTree({'10': ({'9': (None, None)}, {'11': (None, None)})})")
    del root

  def test_insert_on_empty(self):
    root = bt.BinaryTree()
    root.insert(10)
    self.assertEqual(repr(root), "BinaryTree({'10': (None, None)})")
    del root

  def test_remove_on_one_node(self):
    root = bt.BinaryTree(10)
    self.assertEqual(repr(root), "BinaryTree({'10': (None, None)})")
    root.remove(10)
    self.assertEqual(repr(root), "BinaryTree({'None': (None, None)})")

  def test_size(self):
    root = bt.BinaryTree(10)
    root.insert(11)
    root.insert(12)
    root.insert(15)
    self.assertEqual(root.size, 4)

  def test_size_one_node(self):
    root = bt.BinaryTree(10)
    self.assertEqual(root.size, 1)

  def test_size_empty(self):
    root = bt.BinaryTree()
    self.assertEqual(root.size, 0)

  def test_depth(self):
    root = bt.BinaryTree()
    self.assertEqual(root.depth, -1)

  def test_height_two(self):
    root = bt.BinaryTree(12)
    root.insert(11)
    self.assertEqual(root.depth, 1)

  def test_leaves_empty(self):
    root = bt.BinaryTree()
    self.assertEqual(root.leaves, [])

  def test_leaves(self):
    root = bt.BinaryTree(10)
    self.assertEqual(root.leaves, [10])

  def test_leaves_two(self):
    root = bt.BinaryTree(10)
    root.insert(11)
    root.insert(12)
    root.insert(13)
    root.insert(9)
    root.insert(6)
    self.assertEqual(root.leaves, [6,13])

  def test_search_empty(self):
    root = bt.BinaryTree()
    with self.assertRaises(IndexError):
      self.assertFalse(root.search(1337))

  def test_search_exist(self):
    sample = random.sample(range(0, 1000), 100)
    x = sample[-1] # pick right edge case
    root = bt.BinaryTree()
    for v in sample:
      root.insert(v)
    self.assertTrue(root.search(x))

  def test_search_nonexist(self):
    sample = random.sample(range(0, 1000), 100)
    x = 1001
    root = bt.BinaryTree()
    for v in sample:
      root.insert(v)
    self.assertFalse(root.search(x))

class TestLinkedList(unittest.TestCase):
  def test_init(self):
    arr = [1,2,3,4,5]
    ll = array_to_ll(arr)
    self.assertEqual(repr(ll), 'ListNode(1)')
    self.assertEqual(type(ll), ListNode)
    self.assertEqual(str(ll), 'ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))')

  def test_pretty_print(self):
    arr = [1,2,3,4,5]
    ll = array_to_ll(arr)
    self.assertEqual(pprint_linked_list(ll), 'head->1->2->3->4->5->tail')

  def test_merge(self):
    a1 = array_to_ll([1,2,3,4,5])
    a2 = array_to_ll([6,7,8,9,10])
    merged = merge(a1, a2)
    self.assertEqual(list(merged), [1,2,3,4,5,6,7,8,9,10])


if __name__ == "__main__":
  unittest.main()

