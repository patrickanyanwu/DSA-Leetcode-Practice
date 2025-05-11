"""
  Use a heap to get smallest element in O(log n) time and used set to ensure O(1) checks of what numbers are in our heap.
  O(log n) time Pop Smallest. O(log n) time Add Back.
  O(1000) space.
"""

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.setnums = set(self.heap)
        heapify(self.heap)

    def popSmallest(self) -> int:
        if len(self.heap):
            num = heappop(self.heap)
            self.setnums.remove(num)
            return num

    def addBack(self, num: int) -> None:
        if num not in self.setnums:
            self.setnums.add(num)
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
