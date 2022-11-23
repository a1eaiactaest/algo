#!/usr/bin/env python3

import os
import heapq
import networkx as nx

DIRS = [
  (1,0),
  (-1,0),
  (0,1),
  (0,-1),
]

def solve(graph: dict, start: str, end: str):
  visited = set()
  pq = [(0, start)]
  heapq.heapify(pq)

  while len(pq) > 0:
    (cost, cnode) = heapq.heappop(pq)

    if cnode in visited:
      continue
    visited.add(cnode)

    if  cnode == end:
      return cost

    for nnode in graph[cnode]:
      ncost = graph[cnode][nnode]
      if nnode in visited:
        continue
      real_cost = cost + ncost
      heapq.heappush(pq, (real_cost, nnode))
  return -1

def save_graph(d: dict) -> str:
  try:
    graph = nx.Graph(d)
    print('saving', graph)
    nx.drawing.nx_pydot.write_dot(graph, '/tmp/net.dot')
    os.system('dot -Tsvg /tmp/net.dot -o /tmp/net.svg')
  except AttributeError:
    raise AttributeError("Can't create graph from a empty tree. Try adding nodes.")

def main():
  G1 = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

  G2 = {
    "B": {"C": 1},
    "C": {"D": 1},
    "D": {"F": 1},
    "E": {"B": 1, "G": 2},
    "F": {},
    "G": {"F": 1},
  }

  save_graph(G2)
  print(solve(G2, 'B', 'F'))

if __name__ == "__main__":
  main()
