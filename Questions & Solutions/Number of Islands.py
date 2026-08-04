"""Ran a bfs through each cell in the grid that is a 1, the bfs marks every adjacent cell as visited and increments the islands by 1 after that is done. This ensures we dont process any seen island.
O(n * m) time O(n * m) space."""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r, c) not in visited and r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == "1":
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
