from typing import Union, Optional, Any, Iterator

NodeValue = Any

class ListNode:
  """Linked list node.
  Can be treated as a linked list.
  """
  def __init__(self, val:NodeValue=0, next_node:Optional["ListNode"]=None) -> None:
    self.val = val
    self.next = next_node

  def __iter__(self) -> Iterator["ListNode"]:
    cnode = self

    while cnode: 
      nnode = None
      yield cnode.val
      if cnode.next:
        nnode = cnode.next
      cnode = nnode

  def __repr__(self) -> str:
    return f"ListNode({self.val})" 
  
  def __str__(self) -> str:
    return f"ListNode({self.val}, {self.next})" 

  def pretty(self) -> None:
    ret = "head->"
    for node in list(self):
      ret += f"{node}->"
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

def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

  assert isinstance(list1, ListNode), 'list1 is not a linked list'
  assert isinstance(list2, ListNode), 'list2 is not a linked list'

  dummy_head = ListNode()
  tail = dummy_head

  while list1 and list2:
    if list1.val < list2.val:
      tail.next = list1
      list1 = list1.next
    else:
      tail.next = list2
      list2 = list2.next
    tail = tail.next
  if list1:
    tail.next = list1
  elif list2:
    tail.next = list2
  
  return dummy_head.next

if __name__ == "__main__":
  arr = [1,2,3,4,5]
  print(arr)
  ll = array_to_ll(arr)
  print(ll)
  print(list(ll))
  ll.pretty()