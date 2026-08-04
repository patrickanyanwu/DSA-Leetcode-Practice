"""
  Make a bidirectional adjacency list for checking neighbours of a city,
  Run a dfs starting from 0 and for each city if there is not an edge connected to its parent we increment a count as it cant reach 0.
  O(V + E) time O(V) space
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a, b in connections}
        adj = {i: [] for i in range(n)}

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        count = [0]
        seen = set()
        def dfs(city):
            seen.add(city)
            for nei in adj[city]:
                if nei in seen:
                    continue
                if not (nei, city) in edges:
                    count[0] += 1
                seen.add(city)
                dfs(nei)
        dfs(0)
        return count[0]
