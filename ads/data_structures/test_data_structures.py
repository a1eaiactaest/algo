import unittest
import sys

try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO


from binary_tree import *
from linked_list import *

class CaptureOutput(List[str]):
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


def pprint_default(values: List[int]) -> List[str]:
  """Helper function for testing BinaryTree.pprint."""
  root = build_binary_tree(values)
  assert root is not None

  with CaptureOutput() as output:
    root.pprint()

  return [line for line in output if line != ""]

def pprint_linked_list(linked_list) -> str:
  with CaptureOutput() as output:
    linked_list.pretty()
  return ''.join([line for line in output if line != ""])

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

