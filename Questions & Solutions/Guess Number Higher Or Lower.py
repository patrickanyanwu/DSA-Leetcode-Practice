"""
  Run binary search from 0 to n,
  we check the middle between l and r and if it is lower we set l to be m + 1 to find a higher number,
  if out guess was higher we set r to be m - 1 to find a lower guess,
  this divides the guesses by 2 every time allowing for an optimal search.
  O(log n) time O(1) space.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = l + ((r - l) // 2)
            res = guess(m)
            if res < 0:
                r = m - 1
            elif res > 0:
                l = m + 1
            else:
                return m
