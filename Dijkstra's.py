"""
  Used for finding the shortest path from a source node to any node in a graph. We generate our adjacency list and populate it with destination and weight tuples.
  We then initialise a minheap whcih will always keep track of our shortest paths. We at the source node and 0 at first.
  While we have items in our minheap we pop from the minheap (get our path with least weight) and if we have already seen the node (we have already found the shortest path for that node),
  we continue to the next iteration.
  if not we check every node in the current nodes adjacency list and we push the new weight and the node into our heap provided we havent already found a path for that node.
  This guarantees the shorest path for every vertex in our graph.
  O((V + E) * log V) Time O(V + E) space.
  """


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for start, dest, weight in edges:
            adj[start].append((dest, weight))
        shortest = {}
        minheap = [(0, src)]
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    nw = w1 + w2
                    heapq.heappush(minheap, (nw, n2))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
