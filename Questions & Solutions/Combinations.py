"""
I used backtracking with pruning to
generate all combinations. For each number,
I tried including it and excluding it,
building combinations recursively. I added
pruning to skip paths where remaining
numbers can't fill k slots, improving
efficiency by avoiding unnecessary
exploration.
O(C(n,k) * k) time O(k) space
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def dfs(i):
            if len(sol) + (n - i + 1) < k:
                return
            if len(sol) == k:
                res.append(sol[:])
                return
            if i > n:
                return
            sol.append(i)
            dfs(i + 1)
            sol.pop()
            dfs(i + 1)
        dfs(1)
        return res