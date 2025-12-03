"""
I used backtracking to generate all
permutations. At each position, I tried
every number that hasn't been used yet by
checking if it's already in the current
solution. When the solution reaches length
n, I added a copy to results. I backtracked
by removing the last number to try other
possibilities.
O(n! * n) time O(n) space
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def dfs(i):
            if len(sol) == n:
                res.append(sol[:])
            if i >= n:
                return
            if len(sol) > n:
                return
            for j in range(n):
                if nums[j] not in sol:
                    sol.append(nums[j])
                    dfs(i + 1)
                    sol.pop()
        dfs(0)
        return res