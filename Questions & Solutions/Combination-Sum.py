"""For our decision tree we either chose to use the same number again or we don’t. We do this by doing recursive backtracking while running dfs on the list.
Base case is when we reach the case where the sum is greater than the target or i is out of bounds.
If we find a correct sum we append it to our result but we append a copy so that it doesn’t change in res when we perform our backtrack.
O(2^target/min(nums)) time and O(target/min(nums)) space.
"""
#
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol.copy())
                return
            if total > target or i >= len(nums):
                return
            sol.append(nums[i])
            backtrack(i, sol, total + nums[i])
            sol.pop()
            backtrack(i + 1, sol, total)
        backtrack(0, [], 0)
        return res
