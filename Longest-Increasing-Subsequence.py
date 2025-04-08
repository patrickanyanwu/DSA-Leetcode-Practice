"""
  Used a bottom up DP solution here, algorithm works by processing from right to left and keeping track of the length of the longest increasing subsequece from that position,
  For each position we process every number after it and keep track if LIS this way.
  We then return the max of the dp array (longest increasing subsequence).
  O(n^2) time O(n) space
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
