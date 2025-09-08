"""
  We create a result array which wil keep track of how manuy candies for each candidate,
  now we loop from right to left and if the current candidate has a greater rating than the previous we give it 1 more candy than the previousm,
  then we loop from right to left and do the same but checking to the right.
  O(n) time O(n) space
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        
        return sum(res)
