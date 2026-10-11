from functools import cache

"""
Use memoized DFS/DP over (day index, whether we're currently holding a stock).
At each day we have two choices: skip (do nothing, just advance to the next day) or act — buy if we're not holding, or sell if we are.
Buying costs prices[i] and flips the state to holding; selling earns prices[i] but forces a one-day cooldown, so it jumps to i + 2 instead of i + 1 before flipping back to not-holding.
Take the max of acting vs. skipping at each state; @cache memoizes on (i, holding) since the same state can be reached via different past decisions.
O(n) time since there are 2n distinct states each computed once, O(n) space for the cache and recursion stack.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, holding: bool) -> int:
            if i >= n:
                return 0
            skip = dfs(i + 1, holding)                    # do nothing today
            if holding:
                act = prices[i] + dfs(i + 2, False)       # sell, then forced cooldown
            else:
                act = -prices[i] + dfs(i + 1, True)       # buy
            return max(skip, act)

        return dfs(0, False)