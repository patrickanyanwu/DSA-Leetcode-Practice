"""
    We use a sliding window,
    the window increases while the number ahead is greater,
    window closes as soon as we hit a value that isnt greater
    we then constantly update our result with a global max variable
    O(n) time O(1) space
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = r = 0
        res = 1
        while r < len(nums) - 1:
            while r < len(nums) - 1 and nums[r] < nums[r + 1]:
                r += 1
            res = max(res, r - l + 1)
            r += 1
            l = r
        return res