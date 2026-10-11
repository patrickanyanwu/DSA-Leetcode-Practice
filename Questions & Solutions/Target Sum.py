from functools import cache

"""
Use memoized DFS over (index, running total) to count the ways of assigning +/- signs that reach the target.
At each index, branch into two paths: add nums[i] to the running total, or subtract it, then recurse to the next index.
Once every number has been assigned a sign (i == n), this path contributes 1 way if the running total equals target, otherwise 0.
@cache memoizes on (i, total) since the same (index, total) pair can be reached through different sign choices earlier in the recursion, avoiding recomputation.
O(n * s) time/space where s is the range of distinct running totals, since each distinct (i, total) state is computed once.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i: int, total: int) -> int:
            if i == n:
                return 1 if total == target else 0
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)