import os
import sys
from typing import List, Any

try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO

parent = os.path.basename(os.getcwd())
if parent == 'test':
  sys.path.insert(0,'../')

from ads.structures import BinaryTree, build_binary_tree

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
  

if __name__ == "__main__":
  lines = pprint_default([35,28,31,59,23,55,67,50,56,30])
  print(lines)
  lines = pprint_default([10])
  print(lines)
