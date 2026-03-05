"""
This approach uses a max heap to simulate the stone smashing process.
Since Python's heapq implements a min heap, we store negative values to simulate a max heap.
We repeatedly extract the two heaviest stones, and if they have different weights, we push the difference back to the heap.
This continues until at most one stone remains.
O(n log n) time O(n) space.
"""
from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            heap = []
            for stone in stones:
                heappush(heap, -stone)
            while len(heap) >= 2:
                s1, s2 = -heappop(heap), -heappop(heap)
                if s1 != s2:
                    heappush(heap, -(max(s2, s1) - min(s2, s1)))
            return -heap[0] if heap else 0
            