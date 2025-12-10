"""
I used dynamic programming to handle at most k transactions. I maintain
arrays for buy and sell states for each transaction number. When k is large
enough (>= n/2), I can make unlimited transactions, so I use a greedy
approach to capture every upward price movement. For limited k, I iterate
through prices and update each transaction's buy/sell states. For transaction
i, buy[i] is the max profit after buying (considering previous sell), and
sell[i] is the max profit after selling (using current buy). This ensures I
track the best profit for each transaction count up to k.
O(n × k) time O(k) space.
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - p)
                sell[i] = max(sell[i], buy[i] + p)

        return sell[k]