from typing import List, Union
import unittest

def mergesort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
  """Sort passed array in ascending order using merge sort algorithm.

  Time complexity because of recursion is O(n log n)
  """
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

class TestMergeSort(unittest.TestCase):
  def test_case(self):
    arr = [6,6,3,8,1,0,2,4]
    self.assertEqual(mergesort(arr.copy()), sorted(arr))
    del arr

  def test_empty(self):
    arr = []
    self.assertEqual(mergesort(arr.copy()), sorted(arr))
    del arr

