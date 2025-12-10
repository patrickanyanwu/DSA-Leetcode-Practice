class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        I used dynamic programming with space optimization to find the minimum
        path sum from top to bottom. I maintain only the previous row's minimum
        sums instead of the entire DP table. For each position in the current
        row, I compute the minimum sum by adding the current value to the
        minimum of the accessible positions from the previous row. I handle
        edge cases: leftmost positions can only come from the same index above,
        rightmost can only come from one index left, and middle positions can
        come from either adjacent position above. This bottom-up approach
        efficiently computes the answer.
        O(n²) time O(n) space
        """
        n = len(triangle)
        prevrow = [triangle[0][0]]

        for r in range(1, n):
            currow = [float("inf")] * len(triangle[r])
            for c in range(len(currow)):
                if c == 0:
                    currow[c] = prevrow[c] + triangle[r][c]
                elif c == len(currow) - 1:
                    currow[c] = prevrow[c - 1] + triangle[r][c]
                else:
                    currow[c] = min(prevrow[c - 1], prevrow[c]) + triangle[r][c]
            prevrow = currow

        return min(prevrow)