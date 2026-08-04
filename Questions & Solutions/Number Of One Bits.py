"""
  We constantly check for each bit in the integer from right to left, if it is a 1 we increment our cound and if it is a zero we dont.
  We check this by getting the number mod 2 which gives is the last bit of the integer. After each check we rightshift by 1 to focus on the next bit to the left.
  O(1) time O(1) space.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res

"""
  This solution is more efficient as we dont process unnecesary 0's.
  It works by anding the number with the number minus 1 and what this does it it removes a 1 every time from the number,
  O(1) time O(1) space
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
