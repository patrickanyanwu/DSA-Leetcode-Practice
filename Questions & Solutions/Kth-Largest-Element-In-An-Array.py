"""
  Add all numbers to a minhead but use their negative value so it makes it a maxheap.
  Pop from the heap k - 1 times so the new top of the heap will have the kth largest element.
  Return the negative of that number.
  O(n log n) time O(n) space.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, -num)
        for i in range(k - 1):
            heappop(heap)
        return -heap[0]
