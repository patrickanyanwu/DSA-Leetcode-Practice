"""
  Convert edjes to an adjacency list then run a classic dfs through thr graph and mark visited nodes in a set.
  now we loop through each edge and every time we see an unseen node (havent already processed all of its connections)
  we increase out count by 1 and run dfs to mark all connected nodes as visited.
  O(V + E) time and O(V + E) space.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count = 0
        visit = set()
        def dfs(curr):
            visit.add(curr)
            for v in adj[curr]:
                if v not in visit:
                    dfs(v)
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count
