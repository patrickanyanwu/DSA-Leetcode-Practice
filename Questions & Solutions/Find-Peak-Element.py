"""
  We check the number ahead of the middle if the number is less we check to the left,
  if the number is greater we check to the right.
  Because the ends of arrays are considered peaks this guarantees a find.
  O(log n) time O(1) space.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
