class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        I used dynamic programming with space optimization to find the minimum
        path sum from top-left to bottom-right. I initialize the first row with
        cumulative sums since we can only move right. For each subsequent row,
        I compute the minimum sum by choosing the smaller path from either
        above or from the left, then adding the current cell value. For the
        leftmost column, I can only come from above, while other positions can
        come from either direction. I maintain only the previous row to save
        space, updating row by row until reaching the bottom-right corner.
        O(n × m) time O(m) space
        """
        n, m = len(grid), len(grid[0])

        prevrow = [sum(grid[0][:i + 1]) for i in range(m)]
        for r in range(1, n):
            currow = [float("inf")] * m
            for c in range(m):
                cell = grid[r][c]
                if c == 0:
                    currow[c] = cell + prevrow[c]
                else:
                    currow[c] = min(prevrow[c], currow[c - 1]) + cell
            prevrow = currow
        return prevrow[-1]