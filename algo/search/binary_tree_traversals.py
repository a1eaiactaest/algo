from typing import Optional, List

class TreeNode:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def inorder(node: Optional[TreeNode], ret: List[int]=[]) -> List[int]:
  if not node:
    return 
  inorder(node.left, ret)
  ret.append(node.data)
  inorder(node.right, ret)
  return ret

def preorder(node: Optional[TreeNode], ret: List[int]=[]) -> List[int]:
  if not node:
    return 
  ret.append(node.data)
  preorder(node.left, ret)
  preorder(node.right, ret)
  return ret

def postorder(node: Optional[TreeNode], ret: List[int]=[]) -> List[int]:
  if not node:
    return 
  postorder(node.left, ret)
  postorder(node.right, ret)
  ret.append(node.data)
  return ret

def dfs(node: Optional[TreeNode], target: int) -> bool:
  if node.right and not node.left:
    return target == node.val
  return (dfs(node.left, target) or dfs(node.right, target))
  if not node:
    return False

if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(5)
  print(inorder(root))
  print(preorder(root))
  print(postorder(root))
  print(dfs(root, 5))
