"""
I identified regions that shouldn't be
captured by marking all 'O's connected to
the border with a temporary marker 'E' using
DFS. Then I flipped all remaining 'O's to
'X' (they're surrounded) and restored 'E's
back to 'O' (they're connected to borders).
This reverse approach efficiently identifies
non-surrounded regions.
O(m * n) time O(m * n) space
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "E"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"