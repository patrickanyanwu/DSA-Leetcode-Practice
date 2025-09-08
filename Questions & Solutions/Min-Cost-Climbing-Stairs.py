"""
  Bottom up approach while keepting 2 variables,
  1 for if we start from step 0 and the other for if we start with step 1.
  Now we loop through while constantly chosing the minimum between taking 1 step or 2 steps.
  We then return the minumum between the 2 starts.
  O(n) time O(1) sapce
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = cost[0], cost[1]
        for i in range(2, n):
            a, b = b, cost[i] + min(a, b)
        return min(a, b)
