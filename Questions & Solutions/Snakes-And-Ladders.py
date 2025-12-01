"""
I used BFS to find the shortest path from
square 1 to n*n. I converted board positions
to coordinates using a helper function that
handles the alternating row directions. For
each position, I tried all dice rolls (1-6),
checking for snakes/ladders and adding
unvisited squares to the queue. BFS
guarantees the shortest path.
O(n^2) time O(n^2) space
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def square_to_position(square):
            row = n - 1 - (square - 1) // n
            col = (square - 1) % n
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
            return row, col

        q = deque()
        q.append((1, 0))
        visited = set([1])

        while q:
            square, moves = q.popleft()
            if square == n*n:
                return moves

            for step in range(1, 7):
                next_square = square + step
                if next_square > n*n:
                    break

                r, c = square_to_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))

        return -1