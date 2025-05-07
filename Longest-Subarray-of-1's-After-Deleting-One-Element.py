"""
  We keep track of a zero count as we extend our sliding window and if it ever goes above 1 we close our window from the left and decrement 0 count accordingly.
  While doing so we keep track of a maxlength by using r - l and not r - l + 1 as we exclude 1 element.
  O(n) time O(1) space.
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes = 0
        maxCount = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            maxCount = max(maxCount, r - l)
        return maxCount
