"""
  Use xorr operater with every number in the range and every number in the input array.
  The result will be the missing number as exxoring by every other number will result in 0,
  so then the missing number xor 0 will be the missing number.
  O(n) time O(1) space.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        return xorr
