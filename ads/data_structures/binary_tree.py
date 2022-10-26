from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Optional, List, Any, Iterator

import os
from pprint import pformat
import networkx as nx

NodeVal = int | float

class Node:
  def __init__(self, val: int | None = None):
    self.val = val
    self.left: Node | None = None
    self.right: Node | None = None
    self.parent: Node | None = None

  def __repr__(self) -> str:
    s = pformat({f"{self.val}": (self.left, self.right)})
    return f"Node({s})"

class BinaryTree:
  def __init__(self, root: Node | None = None):
    self.root = root

  def __repr__(self) -> str:
    return str(self.root)

  @property
  def empty(self) -> bool:
    return self.root is None

  def _insert_helper(self, val: NodeVal) -> None:
    node = Node(val)
    if self.empty:
      self.root = node
    else:
      p = self.root
      if p is None:
        return None
      while True:
        if val < p.val:
          if p.left is None:
            p.left = node
            break
          else:
            p = p.left
        else:
          if p.right is None:
            p.right = node
            break
          else:
            p = p.right

  def insert(self, *vals: list[NodeVal]) -> None:
    for v in vals:
      self._insert_helper(v)

  def search(self, val: NodeVal) -> Node | None:
    if self.empty:
      raise IndexError("Tree is empty.")
    node = self.root
    while node is not None and node.val is not val:
      if val < node.val:
        node = node.left
      else:
        node = node.right
    return node

  def remove(self, val: NodeVal) -> None:
    parent = None
    cnode = self.root
    if cnode.left is None and cnode.right is None:
      if cnode.val is not None and cnode.val == val:
        cnode.val = None
        return None

    while cnode.val != val:
      parent = cnode
      if val < cnode.val:
        cnode = cnode.left
      else:
        cnode = cnode.right

    # There's no children, current node is a leaf.
    if cnode.right is None and cnode.left is None:
      if parent is not None:
        if parent.left.val == cnode.val:
          parent.left = None
        else:
          parent.right = None
        return self
      else:
        return None

    # There's only right child.
    if cnode.right is not None and cnode.left is None:
      if parent is not None:
        if parent.left.val == cnode.val:
          parent.left = cnode.right
        else:
          parent.right = cnode.right
        return self
      else:
        return cnode.right

    # There's only left child:
    if cnode.right is None and cnode.left is not None:
      if parent is not None:
        if parent.left.val == cnode.val:
          parent.left = cnode.left
        else:
          parent.right = cnode.left
        return self
      else:
        return cnode.left

    # Both children exist
    else:
      if cnode.right.left is not None:
        node = cnode.right.left
        while node.left is not None:
          node = node.left
        self.remove(node.val)
        cnode.val = node.val
        if parent is None:
          return cnode
        else:
          return self

      else:
        cnode.right.left = cnode.left
        if parent is not None:
          if parent.val > cnode.val:
            parent.left = cnode.right
          else:
            parent.right = cnode.right
          return self
        else:
          return cnode.right

def _build_btree_string(root: BinaryTree, rec:bool=False) -> str:
  if root is None:
    return [], 0

  right_child, idx_r = _build_btree_string(root.right, rec=True)
  left_child, idx_l = _build_btree_string(root.left, rec=True)
  
  ret = []

  for i, data in enumerate(right_child):
    if i == idx_r:
      ret.append("  ┌─" + data)
    elif i < idx_r:
      ret.append("    " + data)
    else:
      ret.append("  │ " + data)
  
  ret_idx = len(ret)
  ret.append(f"-({root.data})")

  for i, data in enumerate(left_child):
    if i == idx_l:
      ret.append("  └─" + data)
    elif i > idx_l:
      ret.append("    " + data)
    else:
      ret.append("  │ " + data) 

  if rec:
    return ret, ret_idx
  return '\n'.join(ret)

if __name__ == "__main__":
  l = (8, 3, 6, 1, 10, 14, 13, 4, 7)
  t = BinaryTree()
  for x in l:
    t.insert(x)
  print(t)
  t.remove(10)
  print(t)