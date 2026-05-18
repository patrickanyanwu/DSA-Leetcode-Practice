"""
Iterate over every cell in the grid and start a BFS whenever an unvisited land cell (1) is found.
Mark each visited cell as 0 immediately upon discovery to avoid revisiting and eliminate the need for a separate visited set.
BFS expands in all 4 directions, counting every reachable land cell to get the island's area.
After BFS completes, update the running maximum with the current island's area.
O(n * m) time since each cell is visited at most once, O(n * m) space in the worst case for the BFS queue.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] != 1:
                    continue
                # BFS from this cell
                grid[r][c] = 0
                area = 1
                q = deque([(r, c)])
                while q:
                    row, col = q.popleft()
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            area += 1
                            q.append((nr, nc))
                res = max(res, area)
        return res