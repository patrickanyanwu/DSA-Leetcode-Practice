"""
  For each row in order to get all the characters on each row we use a formula,
  for the first and last rows we add each character in increments of (numrows - 1) * 2,
  and for each row inbetween we increment by our current increment - 2 * the row we are on,
  this gives the next correct character due to the zigzag pattern.
  O(n) time O(n) space.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ""
        for r in range(numRows):
            increment = (numRows - 1) * 2
            for j in range(r, len(s), increment):
                res += s[j]
                if r > 0 and r < numRows - 1 and j + increment - 2 * r < len(s):
                    res += s[j + increment - 2 * r]
        return res
