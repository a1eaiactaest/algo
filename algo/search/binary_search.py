from typing import List, Union, Optional

def binary_search(arr: List[Union[int, float]], target: List[Union[int, float]]) -> Optional[int]:
  """Search for a value in a list using the binary search algorithm.
  
  Iterative approach, pseudo code from wiki.
  https://en.wikipedia.org/wiki/Binary_search_algorithm

  :param arr: Given array.
  :param target: Target value to find in :arr:.
  :return: Index at which :target: is found or None in case :target: is not in :arr:.
  :rtype: int | None
  """

  left = 0
  right = len(arr) - 1

  while left <= right:
    piv = (left + right) // 2
    if arr[piv] < target:
      left = piv + 1
    elif arr[piv] > target:
      right = piv - 1
    else:
      return piv

  return None
