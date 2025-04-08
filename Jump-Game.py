"""
  Greedy: Go from right to left and shift our goal by 1 each time it is possible to get to our goal from that position,
  We then return True if our goal is the beginning of the list and False if otherwise.
  O(n) time O(1) space.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
