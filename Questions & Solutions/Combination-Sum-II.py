"""
For this we sort first so duplicates are adjacent, then we run DFS backtracking with an index so each number is used at most once.
At each recursive level we loop from idx to end, skip duplicate choices for the same level using i > idx and candidates[i] == candidates[i - 1],
and stop early when cur + candidates[i] > target since the array is sorted. If cur == target we append a copy of path to result.
O(2^n * n) time and O(n) space (excluding output).
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res