"""Use memoization to keep previus results in a hashmap, now we can either pick the first number plus the max we can rob from the rest of the array from after the adjacent number.
  Or we can chose from the the rest of the array [1:], we return the max between the 1.
  If the length of nums is 1 we return the number and if the length of nums is 0 we return 0.
  O(n) time O(n) space
"""

class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if tuple(nums) in self.memo:
            return self.memo[tuple(nums)]
        if not nums:
            return 0
        self.memo[tuple(nums)] = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        return self.memo[tuple(nums)]
