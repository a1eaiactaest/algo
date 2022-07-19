import time
from typing import List, Union
from utils import timeit

Sortable = Union[float, int, str]

@timeit
def bubblesort(arr: List[Sortable]) -> List[Sortable]:
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

@timeit
def insertionsort(arr: List[Sortable]) -> List[Sortable]:
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

@timeit
def selectionsort(arr: List[Sortable]) -> List[Sortable]:
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

# Can't really time it with wrapper function, because mergesort is recursive.
def mergesort(arr: List[Sortable]) -> List[Sortable]:
  if len(arr) <= 1:
    return arr
  elif len(arr) == 2:
    if arr[0] > arr[1]:
      return [arr[1], arr[0]]
    else:
      return arr
  
  piv = len(arr)//2
  m1 = mergesort(arr[:piv])
  m2 = mergesort(arr[piv:])

  ret = []
  while True:
    if len(m1) > 0 and len(m2) > 0:
      if m1[0] <= m2[0]:
        ret.append(m1[0])
        m1 = m1[1:]
      else:
        ret.append(m2[0])
        m2 = m2[1:]
    elif len(m1) > 0:
      ret += m1
      m1 = []
    elif len(m2) > 0:
      ret += m2
      m2 = []
    else:
      break
  return ret

@timeit
def time_mergesort(arr: List[Sortable]) -> None:
  print(mergesort(arr))

if __name__ == "__main__":
  arr = [6,6,3,8,1,0,2,4]
  print(bubblesort(arr.copy()))
  print(insertionsort(arr.copy()))
  print(selectionsort(arr.copy()))
  print(mergesort(arr.copy()))

