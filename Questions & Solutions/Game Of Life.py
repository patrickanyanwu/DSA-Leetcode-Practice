"""
  Make a copy of the board in which we will make our state changes,
  we loop through the board and check surrounding cells if they are 1s and keep count,
  we then check against the rules of the game and update our result grid accordingly.
  After that we loop through the board again and copy the results to the board.
  O(n * m) time O(n * m) space
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [[0, -1], [1, -1], [1, 0], [1, 1], 
                      [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        rows, cols = len(board), len(board[0])
        res = [[board[r][c] for c in range(cols)] for r in range(rows)]
        
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        for r in range(rows):
            for c in range(cols):
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if valid(nr, nc) and board[nr][nc] == 1:
                        count += 1
                if board[r][c] == 1:
                    if count < 2 or count > 3:
                        res[r][c] = 0
                else:
                    if count == 3:
                        res[r][c] = 1
        for r in range(rows):
            for c in range(cols):
                board[r][c] = res[r][c]
