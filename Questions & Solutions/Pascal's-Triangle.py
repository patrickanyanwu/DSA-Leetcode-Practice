"""
  Use a 2d array to keep track of results, for loop starts from 1 up untill the num of rows we want,
  i now have a for loop embedded which gets the sum of the 2 numbers in the previous' result at the specific index and the index before it.
  we then append that to our result array then append that array to our dp array to be returned.
  O(n^2) time O(n^2) space
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[1]]
        for r in range(1, numRows):
            res = []
            res.append(1)
            for k in range(1, r):
                prev = dp[r - 1][k] + dp[r - 1][k - 1]
                res.append(prev)
            res.append(1)
            dp.append(res)
        return dp
