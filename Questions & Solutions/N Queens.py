class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        I used backtracking to find all valid N-Queens board configurations.
        I maintain three sets to track attacked positions: columns, positive
        diagonals (r-c), and negative diagonals (r+c). For each row, I try
        placing a queen in each column if it's not under attack. I build the
        board string representation row by row with dots and 'Q'. When I reach
        the last row, I've found a complete valid configuration, so I add it
        to my results. After exploring each placement, I backtrack by removing
        the queen and trying the next position. This explores all possible
        configurations while pruning invalid branches early.
        O(n!) time O(n) space
        """
        col = set()
        posDiag = set() # (r - c)
        negDiag = set() # (r + c)
        res = []
        def backtrack(r, grid):
            if r == n:
                return res.append(grid[:])
            for c in range(n):
                if c in col or (r + c) in negDiag or (r - c) in posDiag:
                    continue
                columnstring = ("." * c) + "Q" + ("." * (n - c - 1))
                col.add(c)
                posDiag.add(r - c)
                negDiag.add(r + c)
                backtrack(r + 1, grid + [columnstring])
                col.remove(c)
                posDiag.remove(r - c)
                negDiag.remove(r + c)
            return False
        backtrack(0, [])
        return res