class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        I tracked row, column, and diagonal sums to determine the winner. I use
        arrays to count moves for each row and column, and variables for both
        diagonals. Player A adds +1 and player B adds -1, alternating with each
        move. After each move, I check if any row, column, or diagonal sum
        reaches absolute value 3, indicating a win. If player is 1 (A's turn
        just completed), A wins; otherwise B wins. I check diagonal conditions
        based on position: main diagonal when r==c, anti-diagonal when r+c==2.
        If no winner and all 9 moves made, it's a draw; otherwise pending.
        O(n) time O(1) space
        """
        rows = [0] * 3
        cols = [0] * 3
        diag = anti = 0

        player = 1

        for r, c in moves:
            rows[r] += player
            cols[c] += player

            if r == c:
                diag += player
            if r + c == 2:
                anti += player

            if (abs(rows[r]) == 3 or
                abs(cols[c]) == 3 or
                abs(diag) == 3 or
                abs(anti) == 3):
                return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == 9 else "Pending"