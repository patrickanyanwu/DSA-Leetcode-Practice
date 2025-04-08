"""
  Bottom up DP approach: we start at the last character of both strings,
  if the letters equal we set the LCS of that cell to be 1 plus the LCS of the cell across from it (which represents the LCS of the previous substring).
  If not we set the LCS of that cell to be the max betwwen the LCS of the cell to the right or the cell below (this choice accounts for if we exclude one letter from one string or the other).
  O(n * m) time O(n * m) space.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
