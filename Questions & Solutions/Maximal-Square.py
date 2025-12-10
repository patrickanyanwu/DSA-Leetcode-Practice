class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        I used dynamic programming to find the largest square of 1s. I create a
        DP table where dp[r][c] represents the side length of the largest
        square with bottom-right corner at (r, c). For cells in the first row
        or column, the max square is 1 if the cell is "1". For other cells, if
        it's "1", I take the minimum of the three adjacent cells (top, left,
        diagonal) and add 1, since all three must form squares for this cell to
        extend them. I track the maximum side length found and return its
        square (area). This efficiently builds up larger squares.
        O(n × m) time O(n × m) space
        """
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_side = 0
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(
                            dp[r - 1][c],
                            dp[r][c - 1],
                            dp[r - 1][c - 1] 
                        )
                    max_side = max(max_side, dp[r][c])

        return max_side * max_side