"""
  We take the equations and turn it into a graph with its weight being its result after the division of the vertices, 
  e.g u -> v would have weight 2 if u / v == 2 and v -> u would have weight 1 / 2 if u / v == 2.
  Now for each query we run a dfs (on u) while multiplying out the weights it took to get to the destination (v) and apppend that result if found else -1
  If 1 or the other of (u or v) is not in out adjacency list then it is impossible to find and we append -1.
  O(n) time O(n) space
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, edge in enumerate(equations):
            u, v = edge
            adj[u].append((values[i], v))
            adj[v].append((1 / values[i], u))
        def dfs(src, dst, visited, acc):
            if src == dst:
                return acc
            visited.add(src)
            for weight, neighbor in adj[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited, acc * weight)
                    if result != -1.0:
                        return result
            return -1.0
        result = []
        for u, v in queries:
            if u not in adj or v not in adj:
                result.append(-1.0)
            elif u == v:
                result.append(1.0)
            else:
                result.append(dfs(u, v, set(), 1.0))

        return result
        
