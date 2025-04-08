"""
  Used a top down DP approach with memoization to stop redundant function calls, for each cell we compute the number of ways we can reach the end and store it in our cache,
  If through our dfs we hit our goal we return 1 and if not we return 0.
  If we meet that cell again we return immediately what the num of ways was from our cache, this brings down the time complexity immensely.
  O(m * n) time O(n * m) space.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row < 0 or col < 0 or row > m or col > n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            memo[(row, col)] = dfs(row, col + 1) + dfs(row + 1, col)
            return memo[(row, col)]
        return dfs(0, 0)
