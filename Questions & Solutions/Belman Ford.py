"""
Bellman-Ford finds shortest paths from a source even with negative edge weights.
Initialize all distances to infinity except the source, which is 0.
Relax every edge up to n-1 times — each full pass guarantees the shortest path using at most that many edges is found, since the longest possible shortest path in a graph with n nodes uses n-1 edges.
Track whether any update happened in a pass; if nothing changed, distances have converged and we can stop early.
After n-1 passes, do one more relaxation pass — if any edge can still be relaxed, a negative-weight cycle exists, so return None.
O(n * e) time since we relax every edge up to n times, O(n) space for the distance array.
"""

def bellman_ford(n, edges, source):
    dist = [float("inf")] * n
    dist[source] = 0

    for _ in range(n - 1):
        updated = False

        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True

        if not updated:
            break

    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return None
    return dist
