"""
  Using variable length sliding window, we keep track of a current 0 count in the window.
  If our zero count ever goes above the max amount of flips we can make we close our window and decrement our 0 count accordingly.
  We keep track of a max every iteration.
  O(n) time O(1) space.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        maxCount = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount
