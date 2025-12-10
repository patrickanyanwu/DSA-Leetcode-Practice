class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        I used state machine dynamic programming to handle at most two
        transactions. I maintain four states: buy1 (max profit after first
        buy), sell1 (max profit after first sell), buy2 (max profit after
        second buy), sell2 (max profit after second sell). For each price, I
        update buy1 as the maximum of keeping it or buying at current price. I
        update sell1 as the maximum of keeping it or selling at current price
        after buy1. Then buy2 considers buying again after sell1, and sell2
        considers selling after buy2. This ensures at most two transactions and
        maximizes profit by considering all possibilities.
        O(n) time O(1) space
        """
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0

        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)

        return sell2