class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        """
        I used dynamic programming in-place to count unique paths while
        avoiding obstacles. I first check if the start is blocked, returning 0
        if so. I initialize the start to 1 path, then process the first row and
        column separately since they can only be reached from one direction. If
        there's an obstacle, I set paths to 0; otherwise, I carry forward the
        previous count. For the rest of the grid, each cell's path count is the
        sum of paths from above and left, unless it's an obstacle (set to 0).
        This in-place approach modifies the grid to store path counts.
        O(n × m) time O(1) space
        """
        n, m = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return 0

        grid[0][0] = 1

        for c in range(1, m):
            grid[0][c] = 0 if grid[0][c] == 1 else grid[0][c - 1]

        for r in range(1, n):
            grid[r][0] = 0 if grid[r][0] == 1 else grid[r - 1][0]

        for r in range(1, n):
            for c in range(1, m):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                else:
                    grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

        return grid[-1][-1]