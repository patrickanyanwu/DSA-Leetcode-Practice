"""
  Cash represents how much cash we have provided we sell a stock or dont,
  hold represents how much share we hold and determines wether we buy a new stock or dont.
  O(n) time O(1) space.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash = 0
        hold = -prices[0]
        for p in prices:
            cash = max(cash, hold + p)
            hold = max(hold, cash -  p)
        return cash
