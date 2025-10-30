"""
    I found the number of bits in n by
    converting to binary, then created a number
    with all bits set by generating a string of
    1s with the same length and converting it
    back to an integer.
    O(log n) time O(log n) space
"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        return int("1" * len(bin(n)[2:]), 2)