"""
  Used bottom up approach but have 3 variables and update them accordingly,
  for each iteration from 3 to n we set our prev to be the sum of the previous 3,
  we set prev2 to just be our prev1 and we set the prev1 to be prev,
  so essentially were shifting the variables up by 1 every time and keeping track of results.
  O(n) time O(1) sapce
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n <= 2:
            return 1
        prev2 = 0
        prev1 = 1
        prev = 1
        for i in range(3, n + 1):
            prev, prev1, prev2 = prev2 + prev1 + prev, prev, prev1
        return prev
