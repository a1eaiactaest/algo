from typing import List, Union
def selectionsort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
  """Sort passed array in ascending order using selection sort algorithm.

  Time complexity of the selection sort is O(n^2)

  Sorts in place, so passed :arr: is changed in it's state. 
  Once sorted, always sorted.

  :param arr: list of values which require sorting. 
  :type arr: sorting.Sortable
  :return: Sorted list of passed values.
  :rtype: sorting.Sortable
  """
  
  for i in range(len(arr)):
    min_i = i # minimum index
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_i]:
        min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]
  return arr
