"""
  Use a max heap to track the maximum element in the current sliding window.
  Store elements as (-value, index) in the heap to simulate max heap using min heap.
  For each position, push the current element to the heap.
  Once we have a complete window (i >= k-1), remove elements from the heap that are outside the window (index <= i-k).
  The top of the heap is always the maximum in the current window.
  O(n log n) time, O(n) space.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output