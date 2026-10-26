"""
Use bottom-up interval DP where dp[l][r] is the max coins from bursting every balloon in the range [l, r].
Pad nums with a 1 on each side so the boundaries always have a neighbor, shifting the real balloons to indices 1..n.
The key trick is to pick i as the LAST balloon burst in [l, r], not the first: by then everything else in the range is gone, so i's neighbors are exactly new_nums[l - 1] and new_nums[r + 1], which sit outside the range and are still intact.
That splits the range into two independent subproblems, dp[l][i - 1] and dp[i + 1][r], so coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1] + dp[l][i - 1] + dp[i + 1][r], and dp[l][r] is the max over every choice of i.
Iterate l from n down to 1 and r from l up to n so both smaller subranges are already filled; empty ranges (l > r) stay 0 as the base case.
The answer is dp[1][n], the whole original array.
O(n^3) time for the three nested loops and O(n^2) space for the dp table.
"""

class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]