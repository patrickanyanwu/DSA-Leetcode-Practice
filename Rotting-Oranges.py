"""
  We run a BFS and keep track of the amount of times we have to rot oranges (how deep we go in our bfs).
  We start by adding all rotten oranges to the queue (multiple source nodes) and we run our bfs and keep track of the max amount of steps we had to take,
  this corresponds to the amount of minutes.
  Return minutes.
  O(m * n) time O(m * n) space.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        while q:
            r, c, m = q.popleft()
            minutes = max(minutes, m)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  
                    fresh -= 1
                    q.append((nr, nc, m + 1))
        return minutes if fresh == 0 else -1
