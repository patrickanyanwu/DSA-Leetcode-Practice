"""Initialize a result string, now i loop bit by bit checking if the bit is a 1 or 0 and add it to our res from right to left,
  After the loop i keep adding 0's untill the length of res is 32 (we have all bits).
  I then convert the string to a base 2 integer and return.
  Works in constant space as the res string will never be greater than 32.
  O(1) time O(1) space.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        while n:
            res += str((n % 2) & 1)
            n >>= 1
        while True:
            if len(res) == 32:
                return int(res, 2)
            res += "0"
