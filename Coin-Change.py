"""
This approach uses DFS with memoization to find the minimum number of coins needed to reach the target amount.
It explores all coin combinations recursively and stores results for each intermediate sum to avoid redundant calculations, significantly improving efficiency.
O(amount * len(coins)) time O(amount) space.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(sum1):
            if sum1 in memo:
                return memo[sum1]
            if sum1 > amount:
                return float('inf')
            if sum1 == amount:
                return 0

            min_coins = float('inf')
            for coin in coins:
                res = dfs(sum1 + coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            memo[sum1] = min_coins
            return memo[sum1]

        result = dfs(0)
        return result if result != float('inf') else -1
