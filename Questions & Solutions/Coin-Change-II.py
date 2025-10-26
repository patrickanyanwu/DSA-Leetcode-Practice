"""
I used dynamic programming to count the number of ways to make the amount. 
I created a dp array where dp[i] represents the number of ways to make amount i. 
I initialized dp[0] = 1 since there's one way to make 0 (use no coins). 
Then, for each coin, I updated all amounts that can be made by adding that coin to previous amounts. 
By iterating through coins in the outer loop, I avoided counting duplicate combinations.
O(n * amount) time O(amount) space.
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]