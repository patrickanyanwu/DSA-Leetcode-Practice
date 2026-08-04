"""
I converted the column number to base-26
representation, treating it as 1-indexed by
decrementing before each division. I built
the result string by prepending characters
from 'A' to 'Z'.
O(log n) time O(log n) space
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1 
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result
            columnNumber //= 26

        return result