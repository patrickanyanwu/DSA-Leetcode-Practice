"""
  Converted the edge list into an adjacency list then run recursive dfs while keeping a seen set to avoid going back to nodes already processed.
  If the current node we are on is equal to the destination node we know we have found a valid path and we return True.
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        seen = set()
        seen.add(source)
        def dfs(start):
            if start == destination:
                return True
            for edge in adjlist[start]:
                if edge not in seen:
                    seen.add(edge)
                    if dfs(edge):
                        return True
        if dfs(source):
            return True
        return False
