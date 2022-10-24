from __future__ import annotations

def find_max(arr: list[int]) -> int:
  m = arr[0]
  for i in range(len(arr)):
    if arr[i] > m:
      m = arr[i]
  return m

def find_max_r(arr: list[int | float], m1: int, m2: int) -> int:
  if m1 == m2:
    return arr[m1]
  mid = (m1 + m2) >> 1
  print(mid)
  left_max = find_max_r(arr, m1, mid)
  right_max = find_max_r(arr, mid+1, m2)
  return left_max if left_max >= right_max else right_max