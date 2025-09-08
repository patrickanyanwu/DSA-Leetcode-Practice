"""
Thought process is the same as my process for house robber I, only change is for the first run of the function we ignore the last number as the bouses are ordered in a circular way.
Every subsequence run can use its last element normally.
O(n) time O(n) space.
"""

class Solution:
    def __init__(self):
        self.memo = {}
        self.count = 0
    def rob(self, nums: List[int]) -> int:
        if self.count == 0:
            self.count += 1
            self.memo[tuple(nums)] = max(nums[0] + self.rob(nums[2:-1]), self.rob(nums[1:]))
        if len(nums) == 1:
            return nums[0]
        if tuple(nums) in self.memo:
            return self.memo[tuple(nums)]
        if not nums:
            return 0
        self.memo[tuple(nums)] = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        return self.memo[tuple(nums)]
