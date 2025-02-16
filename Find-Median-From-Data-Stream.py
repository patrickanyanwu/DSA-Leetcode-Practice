"""Used a min and max heap to keep track of middle numbers, conditionals used to make sure both heaps are balanced and that the max in the max heap is always smaller than the min in the min heap.
When looking for median we check if there is one more element in one of the heaps (odd amount of numbers), in that case we return that middle element,
if not we return the sum of both the min and maxes of the heaps divided by 2. O(log n) time for adding number, O(1) time for getting median so overall O(logn) time and O(n) space."""

from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.smaller, self.larger = [], []

    def addNum(self, num: int) -> None:
        heappush(self.smaller, -num)
        if self.smaller and self.larger:
            if -self.smaller[0] > self.larger[0]:
                curr = heappop(self.smaller)
                heappush(self.larger, -curr)

        if len(self.smaller) > len(self.larger) + 1:
            curr = heappop(self.smaller)
            heappush(self.larger, -curr)

        if len(self.larger) > len(self.smaller) + 1:
            curr = heappop(self.larger)
            heappush(self.smaller, -curr)


    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return self.smaller[0] * -1
        if len(self.larger) > len(self.smaller):
            return self.larger[0]
        return (-self.smaller[0] + self.larger[0]) / 2


        
