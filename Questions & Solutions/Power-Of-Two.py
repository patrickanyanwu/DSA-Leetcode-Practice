"""
    First we check if its negative we return False immetiately,
    Then if not we check the binary representation of the number
    if we only have 1 "1" in the binary we know its a power of 2
    as binary works in base 2.
    O(1) time and space.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return bin(n)[2:].count("1") == 1