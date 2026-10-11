"""
Use memoized DFS/DP over (day index, whether we're currently allowed to buy).
At each day we have two choices: do nothing (cooldown, just advance to the next day) or act — buy if we're in the "buying" state, or sell if we're holding a stock.
Buying costs prices[i] and flips the state to "selling"; selling earns prices[i] but forces a one-day cooldown, so it jumps to i + 2 instead of i + 1 before flipping back to "buying".
Take the max of acting vs. cooling down at each state, and memoize on (i, buying) since the same state can be reached via different past decisions.
O(n) time since there are 2n distinct states each computed once, O(n) space for the memo table and recursion stack.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)