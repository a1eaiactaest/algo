#!/usr/bin/env python3

import os
import sys
import copy
from typing import Union

parent = os.path.basename(os.getcwd())
if parent in ['ADS', 'ads']:
  sys.path.insert(0, 'ads')
elif parent == 'test':
  sys.path.insert(0, '../ads')
  
from trees import BinaryTree, Tree, build

def dfs_binary(tree:BinaryTree) -> list:
  """Traverse through a binary tree using Depth-first search.

  :param tree: Root of the binary tree. 
  :type tree: ads.tree.BinaryTree 
  :return: array of node values stored in :ret: variable.
  :rtype: list

  :info: https://en.wikipedia.org/wiki/Depth-first_search
  """

  ret = []
  stack = []

  stack.append(tree)
  while len(stack) > 0:
    cnode = stack.pop()

    if cnode.right is not None:
      stack.append(cnode.right)

    if cnode.left is not None:
      stack.append(cnode.left)

    if cnode.data is not None:
      ret.append(cnode.data)

  return ret

def bfs_binary(tree:BinaryTree) -> list:
  """Traverse through a binary tree using Breadth-first search.

  :param tree: Root of the binary tree. 
  :type tree: ads.tree.BinaryTree 
  :return: list of BinaryTree.data
  :rtype: list

  :info: https://en.wikipedia.org/wiki/Breadth-first_search
  """

  visited = []
  cdepth = [] 
  ndepth = []

  cdepth.append(tree)

  while len(cdepth) > 0:
    for node in cdepth:
      if node.left is not None:
        ndepth.append(node.left)
      if node.right is not None:
        ndepth.append(node.right)
      if node.data is not None:
        visited.append(node.data)
    cdepth = ndepth
    ndepth = []
  return visited

if __name__ == "__main__":
  x = [35,28,31,59,23,55,67,50,56,30]
  print(dfs_binary(build(x)))
  print(dfs_binary(BinaryTree()))
