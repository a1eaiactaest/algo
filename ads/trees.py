from typing import Union, Optional, Type 

def _build_btree_string(root, rec:bool=False) -> str:
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
  def __init__(self, data=None) -> None:
    self.data = data
    self.right = None
    self.left = None

  def __repr__(self):
    return f"BinaryTree(data={self.data}, right={self.right}, left={self.left})"

  def pprint(self) -> None:
    print(_build_btree_string(self))

  def insert(self, data: Union[int, float]):
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

  def remove(self, data):
    """
    Removes all occurrences of ::data:: in the BinaryTree
    """

    parent = None
    cnode = self

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

def array2bintree(arr: list) -> BinaryTree:
  root = BinaryTree(arr[0])
  for i in range(1, len(arr)):
    root.insert(arr[i])
  return root


if __name__ == "__main__":
  arr = [35,28,31,59,23,55,67,50,56,30]
  bintree = array2bintree(arr)
  bintree.pprint()
  bintree.remove(30)
  bintree.pprint()
  bintree.insert(30)
  bintree.pprint()
