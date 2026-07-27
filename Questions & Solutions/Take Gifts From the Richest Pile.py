"""
Use a max-heap (via negated values) to always access the richest pile in O(log n).
For k rounds, pop the largest pile, take its integer square root using math.isqrt, and push the reduced pile back.
After k rounds, sum the remaining piles (negating back) to get the total gifts left.
O(k log n) time for k heap operations, O(n) space for the heap.
"""

import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -math.isqrt(largest))
        return -sum(heap)