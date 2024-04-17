from typing import List, Union
def insertionsort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
  """Sort passed array in ascending order using insertion sort algorithm.

  Time complexity of the insertion sort is O(n^2)

  Sorts in place, so passed :arr: is changed in it's state. 
  Once sorted, always sorted.

  :param arr: list of values which require sorting. 
  :type arr: sorting.Sortable
  :return: Sorted list of passed values.
  :rtype: sorting.Sortable
  """
  
  for i in range(len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j -= 1
  return arr 
