"""Run recursive backtracking with a seen set in order for us to not use letters at positions we have already checked.
dfs function first checks for the conditions where we return false,
those conditions are if we go out of bounds or if the letter at the current position is not the letter we need,
or if we have went back on a position we have already seen. After that if none of thoe conditions are met we are on a correct letter and can now check the adjacent cells.
We run dfs on all adjacent cells and if any of them return true (we have found a match as i is the length of the word) we return true.
O(n * 4 ^n) time and O(n) space.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in seen:
                return False
            seen.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            seen.remove((r, c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
