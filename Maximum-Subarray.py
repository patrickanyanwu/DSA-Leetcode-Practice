"""
  Used Kadanes algorithm which keeps track of a maxsum and cursum,
  if our cursum is ever below 0 we reset it to 0 as we will never want to add to a negative sum.
  In the case where the numbers are all negative the highest negative number will be returned.
  O(n) time O(1) space.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = nums[0]
        cursub = 0
        for num in nums:
            if cursub < 0:
                cursub = 0
            cursub += num
            currmax = max(cursub, currmax)
        return currmax
