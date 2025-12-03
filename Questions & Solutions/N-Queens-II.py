"""
I used backtracking to count all valid
N-Queens configurations. For each row, I
tried placing a queen in each column,
tracking attacked columns and diagonals
using sets. Positive diagonals use (r - c)
and negative diagonals use (r + c) as keys.
When reaching row n, I incremented the
count. I backtracked by removing queens to
explore other placements.
O(n!) time O(n) space
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        col = set()
        posDiag = set() # (r - c)
        negDiag = set() # (r + c)

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
            for c in range(n):
                if c in col or (r + c) in negDiag or (r - c) in posDiag:
                    continue
                col.add(c)
                posDiag.add(r - c)
                negDiag.add(r + c)
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r - c)
                negDiag.remove(r + c)
        backtrack(0)
        return res