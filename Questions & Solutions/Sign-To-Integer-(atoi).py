"""
I parsed the string by first stripping
whitespace, then checking for a sign.
I built the integer digit by digit while
it remained numeric, applied the sign, and
clamped the result to 32-bit integer bounds.
O(n) time O(1) space
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        res = 0
        
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        res *= sign
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        
        return res