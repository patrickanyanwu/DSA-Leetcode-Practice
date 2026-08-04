"""
I validated whether a string represents a valid number by tracking what I've
seen while iterating. I use flags for digits, decimal points, and exponents.
For each character: digits set the seen_digit flag; +/- signs must be at the
start or immediately after 'e'; decimal points can't appear after 'e' or if
another decimal exists; 'e' requires at least one digit before it and can only
appear once. After seeing 'e', I reset seen_digit to ensure digits follow the
exponent. Any other character is invalid. Finally, I return True only if I've
seen at least one digit. This state-based validation handles all number format
rules efficiently.
O(n) time O(1) space
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_e = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in "+-":
                if i != 0 and s[i - 1].lower() != 'e':
                    return False
            elif ch == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif ch.lower() == 'e':
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            else:
                return False

        return seen_digit
