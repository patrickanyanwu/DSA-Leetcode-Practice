"""
  For each number from 0 to n inclusive we count the number of 1's by constantly anding with the number - 1 (this removes a 1 every iteration).
  Then append the count to our result.
  O(n) time O(n) space.
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            while i:
                i &= (i - 1)
                count += 1
            res.append(count)
        return res
