"""
Use Dijkstra's algorithm to find the shortest path from source node k to all other nodes.
Build an adjacency list from the edge list, then seed a min heap with (0, k) — cost 0 to reach the starting node.
Each iteration pops the cheapest unvisited node, records its cost in dist, and pushes all unvisited neighbours with updated cumulative costs.
Skipping nodes already in dist ensures each node is finalized exactly once with its true shortest distance.
After the heap is exhausted, if all n nodes were reached return the maximum distance (the last node to receive the signal), otherwise return -1.
O((n + e) log n) time where e is the number of edges, O(n + e) space for the adjacency list, heap, and dist map.
"""

from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))

        heap = [(0, k)]
        dist = {}

        while heap:
            cost, node = heappop(heap)
            if node in dist:
                continue
            dist[node] = cost

            for neighbour, weight in adj[node]:
                if neighbour not in dist:
                    heappush(heap, (cost + weight, neighbour))

        return max(dist.values()) if len(dist) == n else -1