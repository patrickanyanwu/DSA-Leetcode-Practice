"""
I converted the column title from base-26
to decimal by iterating through each
character, multiplying the result by 26 and
adding the character's position (A=1, B=2,
etc.).
O(n) time O(1) space
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)

        return result