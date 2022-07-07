#!/usr/bin/env python3

from typing import Union

from trees import BinaryTree, Tree, array2bintree

def dfs_binary(tree:BinaryTree, tail:list=[]) -> list:
  """Traverse through a binary tree using Depth-first search.

  :param tree: Root of the binary tree. 
  :type tree: ads.tree.BinaryTree 
  :param tail: A list used for a tail call in recursion.
  :type tail: list[ads.tree.BinaryTree.data]
  :return: tail
  :rtype: same as tail

  :info: https://en.wikipedia.org/wiki/Depth-first_search
  """

  if tree != None:
    tail.append(tree.data)
    dfs_binary(tree.left, tail)
    dfs_binary(tree.right, tail)
  return tail

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
      visited.append(node.data)
    cdepth = ndepth
    ndepth = []
  return visited

if __name__ == "__main__":
  x = [35,28,31,59,23,55,67,50,56,30]
  tree = array2bintree(x)
  print('dfs ',dfs_binary(tree))
  print('bfs ',bfs_binary(tree))
  tree.pprint()
