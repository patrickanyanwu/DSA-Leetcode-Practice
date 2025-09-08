"""
  Bottom up DP approach, there is only 1 way to reach step 0 and 1,
  now the num of ways to get to the second step is the sum of the num of ways to get to the previous 2 steps (if we come from the previouis step or we come from the previous previous step),
  process repeats n times.
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
