"""
  Run a BFS through the matrix while keeping track of how many steps we took to get to every cell,
  directions array made for easy acces to each next possible direction.
  then if we ever hit an exit (a border) we return the amount of steps it took.
  Seen set used to avoid revisiting cells and we have a check if were at a border and we are at the entrance cell (0 steps have been taken) we continue.
  If exit never found we return -1.
  O(m * n) time O(m * n) space.
"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        def isborder(row, col):
            return row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1
        seen = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        seen.add((entrance[0], entrance[1]))
        while q:
            row, col, step = q.popleft()
            seen.add((row, col))
            if isborder(row, col) and step != 0:
                return step
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r >= 0 and c >= 0 and r < ROWS and c < COLS and (r, c) not in seen:
                    if maze[r][c] != "+":
                        q.append((r, c, step + 1))
                        seen.add((r, c))
        return -1
