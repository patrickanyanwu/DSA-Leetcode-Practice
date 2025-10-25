"""
    n = num of rows in given matrix
    m - num of cols in given matrix
    We start by making a result matrix which will have m rows and n columns,
    as transposes will change the dimensions in that way.
    Now for each cell in the matrix we set the value at result[c][r]
    to the value at matrix[r][c] which puts it in the position it wold be in after a transpose.
    O(n * m) time O(m * n) space.
    """

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res[c][r] = matrix[r][c]
        return res
