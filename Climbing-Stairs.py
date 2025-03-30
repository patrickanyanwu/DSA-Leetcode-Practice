"""
  Start from the final stair, count the sum of the amount of ways i can reach the top from the previous 2 steps which will be the amount of ways i can get up from the previous step.
  This way we are guaranteed the number of ways to get to the nth step.
  O(n) time O(1) space.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1

        for i in range(n):
            temp = one
            one = two + one
            two = temp
        return two
