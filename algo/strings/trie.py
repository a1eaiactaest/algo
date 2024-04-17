#!/usr/bin/env python3

import os
import collections
import networkx as nx

from typing import Iterator

class TrieNode:
  def __init__(self):
    self.children = collections.defaultdict(list)
    self.word = False

  def __str__(self) -> str:
    return str(self.children)

  def __repr__(self) -> str:
    return str(self.children)

  def __iter__(self) -> Iterator[str]:
    return iter(self.children)

class Trie:
  def __init__(self,):
    self.root = TrieNode()

  def __str__(self) -> list[str]:
    return str(self.root)

  def insert(self, word: str) -> None:
    current = self.root

    for c in word:
      if c not in current.children:
        current.children[c] = TrieNode()
      current = current.children[c]
    current.word = True

  def search(self, word: str) -> bool:
    current = self.root

    for c in word:
      if c not in current.children:
        return False
      current = current.children[c]
    return current.word

  def starts_with(self, prefix: str) -> bool:
    current = self.root
    for c in prefix:
      if c not in current.children:
        return False
      current = current.children[c]
    return True

  def _iter_helper(self, node: TrieNode=None, path: list[str]=[]) -> list[str]:
    if node is None: node = self.root
    if node.word: return

    for char, child in node.children.items():
      path.append(char)
      self._iter_helper(child, path)
    return path

  def __iter__(self) -> Iterator[str]: return iter(self._iter_helper())

  def _create_graph(self, *args, **kwargs) -> nx.DiGraph:
    G = nx.DiGraph()
    G.add_nodes_from(self.root.children.keys())
    for k,v in self.root.children.items():
      G.add_edges_from([(k,t) for t in v])
    return G

  @property
  def graph(self) -> nx.DiGraph:
    return self._create_graph()

def save_graph(T: Trie) -> None:
  try:
    graph = T.graph
    print(f'saving {graph} to /tmp/net.svg')
    nx.drawing.nx_pydot.write_dot(graph, '/tmp/net.dot')
    os.system('dot -Tsvg /tmp/net.dot -o /tmp/net.svg')
  except AttributeError:
    raise AttributeError("Can't create graph from an empty tree. Try adding nodes")

if __name__ == "__main__":
  t = Trie()
  print(t)
  t.insert('dupa')
  t.insert('kupa')
  t.insert('abcd')
  t.insert('defg')
  t.insert('jask')
  print(t)
  print(list(t))
  save_graph(t)