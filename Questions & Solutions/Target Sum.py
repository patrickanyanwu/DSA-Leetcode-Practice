from collections import defaultdict

"""
Use bottom-up DP where dp maps each reachable running sum to the number of sign assignments that produce it.
Start with dp = {0: 1}, since before placing any numbers there is exactly one way to have a sum of 0.
For each num, build next_dp from dp: every existing sum branches into cur_sum + num and cur_sum - num, each inheriting that sum's count.
Different sign choices that land on the same sum merge into one entry, so counts are added instead of tracking every path separately.
After processing all numbers, dp[target] is the number of ways to reach the target (0 if it was never reached, thanks to defaultdict).
O(n * s) time and O(s) space, where s is the number of distinct running sums (at most 2 * sum(nums) + 1), since only the previous layer is kept.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i, num in enumerate(nums):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + num] += count
                next_dp[cur_sum - num] += count
            dp = next_dp
        
        return dp[target]