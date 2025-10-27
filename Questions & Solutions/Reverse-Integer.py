"""
I reversed the integer by extracting digits
from the most significant position and
building the result from least to most
significant. I tracked the sign separately
and checked for 32-bit overflow before
returning.
O(log n) time O(1) space
"""

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        base = 1
        negative = x < 0
        x = abs(x)
        tmp = x
        length = 0
        while tmp:
            tmp //= 10
            length += 1
        while x and length:
            res += ((x // (10 ** (length - 1))) * base)
            x %= (10 ** (length - 1))
            base *= 10
            length -= 1
        if res >= 2 ** 31 - 1:
            return 0
        return -res if negative else res