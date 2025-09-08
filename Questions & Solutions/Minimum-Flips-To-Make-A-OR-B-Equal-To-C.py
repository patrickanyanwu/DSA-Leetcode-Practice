"""
  We constantly look at the rightmost bit and check if a's rightmost bit or b's rightmost bit is equal to c's righmost bit.
  If it is not we check if c's bit is a 0, if it is we see if a's bit is equal to c's bit that means a is 1 and b is 1 and c is 0
  we need to flip both and b's bits so we increment our count by 2 instead of 1, all other cases we incrment our count by 1 as we would only
  need yo flip 1 bit. We do this while a or b is not equal to c, once it is we return our count as no more flips need to be made.
  O(log n) time O(1) space
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        while (a | b != c):
            curbit = c % 2
            abit = a % 2
            bbit = b % 2
            curor = abit | bbit
            if curor != curbit:
                if curbit == 0:
                    if abit == bbit:
                        count += 2
                    else:
                        count += 1
                else:
                    count += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return count
