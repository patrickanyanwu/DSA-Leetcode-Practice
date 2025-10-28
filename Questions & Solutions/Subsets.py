"""
    I used backtracking to generate all subsets
    by making two choices at each position:
    include the current element or exclude it.
    I recursed through all elements and copied
    each valid subset to the result.
    O(2^n * n) time O(n) space
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i >= n:
                res.append(sol[:])
                return
            backtrack(i + 1)
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        backtrack(0)
        return res