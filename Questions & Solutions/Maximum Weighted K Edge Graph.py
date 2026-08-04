"""
I used DFS with memoization to explore all possible paths of exactly k edges.
Starting from each node, I recursively explored neighbors while tracking the total weight and depth.
I memoized states to avoid recomputation and returned -1 if the total exceeded the threshold t or no 
valid path existed.
O(n * t * k) time O(n * t * k + E) space
"""

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        adj = {i: [] for i in range(n)}
        memo = {}

        for u, v, w in edges:
            adj[u].append((v, w))
        
        def dfs(curr, total, depth):
            if (curr, total, depth) in memo:
                return memo[(curr, total, depth)]

            if total >= t:
                return -1
            if depth == k:
                return total
            
            cur_res = -1
            for neighbor, w in adj[curr]:
                cur_res = max(cur_res, dfs(neighbor, total + w, depth + 1))

            memo[(curr, total, depth)] = cur_res
            return cur_res

        result = -1
        for i in range(n):
            result = max(result, dfs(i, 0, 0))
        return result