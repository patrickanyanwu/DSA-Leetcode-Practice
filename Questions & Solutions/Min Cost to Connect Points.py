"""
Treat every point as a node and use Kruskal's algorithm to build a minimum spanning tree.
Generate an edge between every pair of points weighted by their Manhattan distance.
Sort all edges by cost ascending so the cheapest connections are considered first.
Use Union-Find to add an edge only if it connects two previously separate components (union by rank, with path compression in find), avoiding cycles.
Sum the cost of every edge that successfully unions two components — once all points are connected, this sum is the minimum cost.
O(n^2 log n) time dominated by generating and sorting the n^2 edges, O(n^2) space for the edge list.
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points = list(map(tuple, points))
        edges = []

        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                cost = distance(x1, y1, x2, y2)

                edges.append([cost, (x1, y1), (x2, y2)])

        edges.sort(key= lambda x:x[0])

        parent = {point: point for point in points}
        rank = {point: 0 for point in points}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return False
            
            if rank[px] < rank[py]:
                px, py = py, px

            parent[py] = px

            if rank[px] == rank[py]:
                rank[py] += 1
            
            return True

        res = 0

        for cost, u, v in edges:
            if union(u, v):
                res += cost
        
        return res