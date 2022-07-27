from dataclasses import dataclass
from typing import Union, Optional, List, Any, Iterator

import os
import networkx as nx

NodeValue = Any

def _build_btree_string(root, rec:bool=False) -> str:
  """Represents binary tree in a visual format.

  :param root: Root of the binary tree.
  :type root: BinaryTree
  :param rec: true if recursive call is made.
  :type rec: Optional[bool]
  :default ret: False
  :return: Visual representation of a binary tree.
  :rtype: str
  """

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

class BinaryTree:
  def __init__(self, data:Optional[NodeValue]=None) -> None:
    self.data = data
    self.right = None
    self.left = None

  def __repr__(self):
    return f"BinaryTree(data={self.data}, right={self.right}, left={self.left})"

  def __eq__(self, other):
    return self.data == other

  def __ne__(self, other):
    return self.data != other

  def __iter__(self) -> Iterator["BinaryTree"]:
    """Iterate through the nodes in the binary tree.
    
    :return: BinaryTree iterator
    :rtype: Iterator[trees.BinaryTree]
    """

    cdepth = [self]

    while len(cdepth) > 0:
      ndepth = []
      for node in cdepth:
        yield node

        if node.left is not None:
          ndepth.append(node.left)
        if node.right is not None:
          ndepth.append(node.right)
      cdepth = ndepth

  def pprint(self) -> None:
    print(_build_btree_string(self))

  def insert(self, data: Union[int, float]) -> "BinaryTree":
    """Adds data to a binary tree.

    :param data: Value which should be added to the tree.
    :type data: NodeValue
    :return: Mdodified binary tree.
    :rtype: BinaryTree
    """
    if self.data == None:
      self.data = data
      return

    if data == self.data:
      return

    if data < self.data and self.left is not None:
      return self.left.insert(data)
    if data > self.data and self.right is not None:
      return self.right.insert(data)

    new_node = BinaryTree(data)
    if data < self.data and self.left is None:
      self.left = new_node
    if data > self.data and self.right is None:
      self.right = new_node
    return

  def remove(self, data: NodeValue) -> "BinaryTree":
    """Removes all occurrences of ::data:: in the BinaryTree

    :param data: Value which should be removed from a tree.
    :type data: NodeValue
    :return: Modified Binary Tree without :data:
    :rtype: BinaryTree
    """

    parent = None
    cnode = self

    if self.left is None and self.right is None:
      if self.data is not None and self.data == data:
        self.data = None
        return

    while cnode.data != data:
      if data < cnode.data:
        parent = cnode
        cnode = cnode.left
      else:
        parent = cnode
        cnode = cnode.right

    # There's no children, current node is a leaf.
    if cnode.right is None and cnode.left is None:
      if parent is not None:
        if parent.left.data == cnode.data:
          parent.left = None
        else:
          parent.right = None
        return self
      else:
        return None

    # There's only right child.
    if cnode.right is not None and cnode.left is None:
      if parent is not None:
        if parent.left.data == cnode.data:
          parent.left = cnode.right
        else:
          parent.right = cnode.right
        return self
      else:
        return cnode.right

    # There's only left child.
    if cnode.right is None and cnode.left is not None:
      if parent is not None:
        if parent.left.data == cnode.data:
          parent.left = cnode.left
        else:
          parent.right = cnode.left
        return self
      else: 
        return cnode.left
    
    # Both children exist.
    else:
      if cnode.right.left is not None:
        node = cnode.right.left
        while node.left is not None:
          node = node.left
        self.remove(node.data)
        cnode.data = node.data
        if parent is None:
          return cnode
        else:
          return self

      else:
        cnode.right.left = cnode.left
        if parent is not None:
          if parent.data > cnode.data:
            parent.left = cnode.right
          else:
            parent.right = cnode.right
          return self
        else:
          return cnode.right

  @property
  def leaves(self) -> List["BinaryTree"]:
    """Return the leaf nodes of the binary tree.

    Leaf nodes are the one without any children.

    :return: List of leaf nodes.
    :rtype [ads.trees.BinaryTree]
    """

    cdepth= [self]
    leaves = []

    while len(cdepth) > 0:
      ndepth = []
      for node in cdepth:
        if node.left is None and node.right is None:
          if node.data is not None:
            leaves.append(node.data)
            continue
        if node.left is not None:
          ndepth.append(node.left)
        if node.right is not None:
          ndepth.append(node.right)
      cdepth = ndepth
    return leaves

  @property
  def height(self) -> int:
    """Return the height of the binary tree.

    Height is the number of edges on the longest path between a root and a leaf node.
    Binary tree with a single node (root) has height of 0.

    :return: Height of a binary tree.
    :rtype: int
    """
    return _get_bintree_properties(self).height

  @property
  def size(self) -> int:
    """Returns the size of the binary tree.

    Size is the number of nodes in the binary tree.

    :return: Number of all nodes in the binary tree.
    :rtype: int
    """
    return _get_bintree_properties(self).size

  def _create_graph(self, *args: Any, **kwargs: Any) -> nx.DiGraph:
    """Create networkx Directional Graph

    This is a helper method.
    """
    digraph = nx.DiGraph(*args, **kwargs)

    for node in self:
      digraph.add_node(node.data)

      if node.left is not None:
        digraph.add_edge(node.data, node.left.data)
      if node.right is not None:
        digraph.add_edge(node.data, node.right.data)

    return digraph

  @property
  def graph(self) -> nx.DiGraph:
    """Create and return networkx Directional Graph.
    """
    return self._create_graph(self)

  def save_graph(self) -> None:
    """Save networkx Directinal Graph as dot file and then convert it to the svg file.
    
    **Usage: ** 

      >> T = BinaryTree(12)
      >> T.insert(11)
      >> T.insert(13)
      >> T.graph
      <networkx.classes.digraph.DiGraph at 0x1113f8d60>

      >> T.save_graph()
      saving DiGraph with 3 nodes and 2 edges

      # Now open file:///tmp/net.svg in your browser.
      # SVG is rendered from dot file using graphviz. 

    """
    graph = self._create_graph()
    print("saving", graph)
    nx.drawing.nx_pydot.write_dot(graph, '/tmp/net.dot')
    os.system('dot -Tsvg /tmp/net.dot -o /tmp/net.svg')

@dataclass
class BinaryTreeProperties:
  height: int
  size: int
  is_complete: bool
  leaf_count: int
  min_node: NodeValue
  max_node: NodeValue

def _get_bintree_properties(root: BinaryTree) -> BinaryTreeProperties:
  min_node = root.data
  max_node = root.data
  size = 0
  leaf_count = 0
  min_leaf_depth = 0
  max_leaf_depth = -1
  is_complete = True
  none_node_seen = False

  cdepth = [root]
  while len(cdepth) > 0:
    max_leaf_depth += 1
    ndepth = []

    for node in cdepth:
      data = node.data
      if data is not None:
        size += 1
        min_node = min(data, min_node)
        max_node = min(data, max_node)

        if node.left is None and node.right is None:
          if min_leaf_depth == 0:
            min_leaf_depth = max_leaf_depth
          leaf_count += 1

        if node.left is not None:
          ndepth.append(node.left)
          is_complete = not none_node_seen
        else:
          none_node_seen = True

        if node.right is not None:
          ndepth.append(node.right)
          is_complete = not none_node_seen
        else:
          none_node_seen = True

    cdepth = ndepth
  
  return BinaryTreeProperties(
    height=max_leaf_depth,
    size=size,
    is_complete=is_complete,
    leaf_count=leaf_count,
    min_node=min_node,
    max_node=max_node
  )


def build_binary_tree(arr: List[NodeValue]) -> BinaryTree:
  """Build a tree from list and return it's node.

  :param arr: List representation of a tree, which is a list of node values.
  :type arr: [Any]
  :return: Root node of created binary tree.
  :rype: BinaryTree
  """

  root = BinaryTree(arr[0])
  for i in range(1, len(arr)):
    root.insert(arr[i])
  return root

class AVLTree:
  def __init__(self, data:NodeValue=None):
    self.data = data
    self.left = None
    self.right = None

  def __eg__(self):
    pass

class RedBlackTree(BinaryTree):
  def __init__(self, data:Optional[NodeValue]=None) -> None:
    super().__init__(data)

    self.red = True
    self.black = not self.red

class ListNode:
  """Linked list node.
  Can be treated as a linked list.
  """
  def __init__(self, val:NodeValue=0, next_node:Optional["ListNode"]=None):
    self.val = val
    self.next = next_node

  def __iter__(self) -> Iterator["ListNode"]:
    cnode = self

    while cnode: 
      nnode = None
      yield cnode
      if cnode.next:
        nnode = cnode.next
      cnode = nnode

  def __repr__(self) -> str:
    return f"ListNode({self.val})" 

  def pretty(self) -> None:
    ret = "head->"
    for node in list(self):
      ret += f"{node.val}->"
    ret += "tail"
    print(ret)

def array_to_ll(arr: list):
  """Given array create a linked list.

  Input: [1,2,3,4,5]
  Output: 1->2->3->4->5->null

  :param arr: input array 
  :type arr: list
  :return: Linked list containing values from :arr:
  :rtype: ListNode
  """

  dummy = ListNode()
  tail = dummy

  for elem in arr:
    tail.next = ListNode(elem)
    tail = tail.next
  return dummy.next

if __name__ == "__main__":
  #arr = [35,28,31,59,23,55,67,50,56,30]
  arr = [1,2,3,4,5]
  ll = array_to_ll(arr)
  print(ll)
  print(list(ll))
  ll.pretty()
