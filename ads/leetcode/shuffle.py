from typing import List

# reference: https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums: List[int], n: int) -> List[int]:
  ret = []
  for x,y in zip(nums[:n], nums[n:]):
      ret.append(x)
      ret.append(y)
  return ret

if __name__ == "__main__":
  nums = [1,2,3,4,4,3,2,1]
  n = 4
  assert shuffle(nums, n) == [1,4,2,3,3,2,4,1], 'err'

