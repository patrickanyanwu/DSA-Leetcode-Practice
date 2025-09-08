"""
  We have a result array for our result and a path array for our current path we are chosing,
  Now our backtrack function takes 1 parameter our current valid start for our range of numbers 
  (as we cant chose 1 number twice), now for each function called we do a loop in the range from start to 10 non inclusive
  and we consider each number in our path and pop them (backtrack) after we have considered them.
  O((N C K) * k) time O((N C K) * k) space.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start):
            left = k - len(path)
            remaining = n - sum(path)
            if left == 0:
                if remaining == 0:
                    res.append(path.copy())
                return
            if remaining < 0:
                return
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1)
                path.pop()
        backtrack(1)
        return res
