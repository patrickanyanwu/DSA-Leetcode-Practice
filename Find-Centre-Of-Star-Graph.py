"""Convert edge list to adjacency list then check whichever vertex has all of the other nodes in the graph as its edges it is the centre of the graph."""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        adjlist = defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        for v, edge in adjlist.items():
            if len(edge) == n:
                return v
