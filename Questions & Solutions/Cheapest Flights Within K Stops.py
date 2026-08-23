"""
Use a modified Dijkstra where the priority queue orders by cost but state also tracks how many stops (edges) were used to get there.
Build an adjacency list of (neighbour, price) from the flights.
Pop the cheapest (cost, node, stops) from the heap; if it's the destination, that's the cheapest price found so it's the answer.
Skip a state if it already used more than k stops, or if a cheaper-or-equal path already reached this node with fewer or equal stops (best_stops[node] tracks the fewest stops seen at that node so far) — this avoids paths that are both more expensive and use more stops than one already explored.
Otherwise relax every outgoing edge, pushing the new cost and incremented stop count onto the heap.
O(e * k log(e * k)) time in the worst case since a node can be revisited once per distinct stop count, O(n + e) space for the graph plus O(e * k) for the heap.
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        best_stops = [float('inf')] * n

        # (total_cost, node, edges_used)
        pq = [(0, src, 0)]

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue

            if stops >= best_stops[node]:
                continue
            
            best_stops[node] = stops

            for nei, w in graph[node]:
                heapq.heappush(pq, (cost + w, nei, stops + 1))

        return -1