"""
  Convert matrix to adjacency list,
  Now we run dfs on each node we havent already seen and we increment a count for every dfs we had to do.
  This gives us the number of connected vertices in the graph.
  O(V ^ 2) time O(V) space
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if j != i and isConnected[i][j]:
                    adj[i].append(j)
        seen = set()
        def dfs(cur):
            seen.add(cur)
            for v in adj[cur]:
                if v not in seen:
                    dfs(v)
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count
