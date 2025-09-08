"""Run DFS through graph and if a cycle is detected we return valse.
How we avoid going back the the previous node we came from due to the graph being undirected we use a prev valeus throughout the DFS.
If at any point we find a loop (we go back to a node that was visited) we return False.
Our final check is that all nodes we vvisited is porportional to the amount of nodes in the graph (all nodes are connected in the graph).
O(V + E) time O(V + E) space
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 < len(edges):
            return False
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for v, e in edges:
            adj[v].append(e)
            adj[e].append(v)
        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for v in adj[curr]:
                if v == prev:
                    continue
                if not dfs(v, curr):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n
