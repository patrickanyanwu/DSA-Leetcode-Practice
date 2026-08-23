"""
Use Dijkstra-style search with a min-heap, where the "distance" to a cell is the highest elevation encountered so far on the best path to reach it.
Start at (0, 0) with cost equal to its own elevation, and mark it seen.
Repeatedly pop the cell with the smallest current cost; if it's the bottom-right cell, that cost is the answer since it's the minimum time needed to have a connected path there.
For each unseen neighbour, the cost to reach it is the max of the current path's cost and the neighbour's own elevation (you must wait for the water to rise to at least that height), push it onto the heap and mark it seen.
O(n^2 log n) time since each of the n^2 cells is pushed and popped from the heap once, O(n^2) space for the heap and seen set.
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        heap = [(grid[0][0], (0, 0))]
        seen.add((0, 0))

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n

        while heap:
            t, (x, y) = heapq.heappop(heap)
            
            if x == y and y == n - 1:
                return t
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    if (nx, ny) not in seen:
                        time = max(t, grid[nx][ny])
                        heapq.heappush(heap, (time, (nx, ny)))
                        seen.add((nx, ny))