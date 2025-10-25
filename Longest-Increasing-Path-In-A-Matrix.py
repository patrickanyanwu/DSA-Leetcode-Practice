"""
    For each cell we run a dfs and we keep track of a memo,
    now after computing the longest increasing path from that cell
    we store that value in the memo and if we ever hit a cell thats
    in the memo we return that value immediately.
    We then return the max result weve gotten accross all cells.
    O(n * m) time O(n * m) space
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            longest = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))
            
            memo[(r, c)] = longest
            return longest

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c))
        
        return result