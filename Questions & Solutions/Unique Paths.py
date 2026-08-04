"""
  Top down solution: Used a top down DP approach with memoization to stop redundant function calls,
  for each cell we compute the number of ways we can reach the end and store it in our cache,
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

"""
  Bottom up solution: The first row at the bottom and the last column always only has one way of getting to the end,
  So for each subsequent row above we calculate the number of paths by adding the number of paths we can go from the right cell + the bottom cell.
  We then update our previous row accordingly which allows for O(n) sapce.
  O(m * n) time O(n) space.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newrow = [1] * n
            for j in range(n - 2, -1, -1):
                newrow[j] = row[j] + newrow[j + 1]
            row = newrow
        return row[0]
