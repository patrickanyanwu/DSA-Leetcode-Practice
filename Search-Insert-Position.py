"""
  Use binary search and return m if we happen to find the number in the array already as that would be its insert position,
  if we dont find it we return l which would be pointing at the insert position due to how binary search works.
  O(log n) time O(1) space
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return l
