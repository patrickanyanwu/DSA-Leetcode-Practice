class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        I used dynamic programming in-place to find the largest square of 1s. I
        convert each cell from string to integer while iterating. For each cell
        with value 1, if it's not in the first row or column, I compute the
        side length of the largest square ending at that position by taking the
        minimum of the three adjacent cells (top, left, diagonal) and adding 1.
        This works because all three positions must form valid squares for the
        current cell to extend them. I track the maximum side length found
        throughout and return its square (area).
        O(n × m) time O(1) space
        """
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        max_side = 0
        
        for r in range(n):
            for c in range(m):
                matrix[r][c] = int(matrix[r][c])
                if r > 0 and c > 0 and matrix[r][c] == 1:
                    matrix[r][c] = 1 + min(
                        matrix[r - 1][c],
                        matrix[r][c - 1],
                        matrix[r - 1][c - 1] 
                    )
                max_side = max(max_side, matrix[r][c])

        return max_side * max_side