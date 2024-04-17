from typing import List, Union

def bubblesort(arr: List[Union[int,float]]) -> List[Union[int,float]]:
  """Sort passed array in ascending order using bubble sort algorithm.

  Time complexity of the bubble sort is O(n^2)

  Sorts in place, so passed :arr: is changed in it's state. 
  Once sorted, always sorted.

  :param arr: list of values which require sorting. 
  :type arr: sorting.Sortable
  :return: Sorted list of passed values.
  :rtype: sorting.Sortable
  """

  for i in range(len(arr)):
    for j in range(i):
      if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i] # swap
  return arr