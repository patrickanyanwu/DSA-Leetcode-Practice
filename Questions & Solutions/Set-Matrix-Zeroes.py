"""
  As we iterate threough the matrix if we encounter a zero we set the first row at that column to 0 and the first column for that row to 0 so that we can use it as an indication later in our code.
  If the first row has a zero we mark that with a variable instead just to cover this edge case later.
  Now we check for each cell if the top row at that column is a zero of the first column of that row is a zero we know we need to change that to a zero.
  We then do our checks for if the top row should be zeroed out or the leftmost column should be zeroed out.
  O(n * m) time O(1) space
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
