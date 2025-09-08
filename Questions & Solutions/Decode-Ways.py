"""
  Took a recursive backtracking approach with memoization to ensure linear time complexity. 
  for each index we can either process the next singular character or we can process the next 2 characters.
  So we run our recursive dfs while choosing either one element or 2 elements and if we ever reach the end of our string we have a valid sequence.
  we hold the number of ways in a result variable and return that result variable.
  O(n) time O(n) space.
"""

class Solution:
    def __init__(self):
        self.memo = {}
    def numDecodings(self, s: str) -> int:
        
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or 
                   (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)
            self.memo[i] = res
            return self.memo[i]

        return dfs(0)
