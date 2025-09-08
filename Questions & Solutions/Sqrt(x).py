"""
  Run binary search to find the m that squared gives x,
  if we dont find it (its sqrt isnt an integer) we return r as r will be pointing to the closest possible integer to the sqrt.
  O(log n) time O(1) space
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = l + (r - l) // 2
            msq = m * m
            if msq < x:
                l = m + 1
            elif msq > x:
                r = m - 1
            else:
                return m
        return r
