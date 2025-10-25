"""
    Use a sliding window which increases while we have a 1,
    once we hit a 0 we increment r and set l to be r (to close out window).
    As our window opes we keep track of a max length.
    O(n) time O(1) space
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(nums):
            while r < len(nums) and nums[r] == 1:
                res = max(res, r - l + 1)
                r += 1
            r += 1
            l = r
        return res