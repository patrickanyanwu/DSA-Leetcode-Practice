"""
This approach uses a min heap to find the k closest points to the origin.
We calculate the distance (using squared Euclidean distance to avoid sqrt) for each point and store it with the coordinates in a heap.
Then we pop k times from the min heap to get the k closest points.
O(n + k log n) time O(n) space.
"""
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res