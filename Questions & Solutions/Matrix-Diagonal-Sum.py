class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        I calculated the sum of both diagonals by iterating through rows and
        using an offset variable. For each row r, I add the primary diagonal
        element at mat[r][offset] and the secondary diagonal element at
        mat[r][n-1-offset]. I check if the indices are different before adding
        the secondary diagonal to avoid counting the center element twice in
        odd-sized matrices. The offset increments with each row, moving both
        diagonal positions. This single-pass approach efficiently sums both
        diagonals while handling the overlap case.
        O(n) time O(1) space
        """
        offset = 0
        res = 0
        for r in range(len(mat)):
            res += mat[r][offset]
            if offset != len(mat) - 1 - offset:
                res += mat[r][len(mat) - 1 - offset]
            offset += 1
        return res