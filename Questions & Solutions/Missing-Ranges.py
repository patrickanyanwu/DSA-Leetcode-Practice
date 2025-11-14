"""
I checked for gaps before the first number,
between consecutive numbers, and after the
last number. For each gap larger than 1, I
added the missing range to the result list.
O(n) time O(1) space
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        res = []
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])
        for l in range(1, len(nums)):
            if nums[l] - nums[l - 1] == 1:
                continue
            res.append([nums[l - 1] + 1, nums[l] - 1])
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        return res