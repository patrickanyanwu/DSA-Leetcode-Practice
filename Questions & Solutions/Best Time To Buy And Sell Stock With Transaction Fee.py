"""
  We maintain two variables, cash and hold, as we scan the price array:
  cash is the best profit so far when not holding a share, at each day we either keep our cash or sell our held share (paying the fee),
  and hold is the best (possibly negative) profit when holding a share at each day we either keep holding or buy today (deducting today’s price from cash).
  We initialize cash = 0 and hold = −prices[0], then for each price update.
  O(n) time O(1) space.
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for p in prices:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        return cash
