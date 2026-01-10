"""
I implemented a circular queue using a fixed-size array with front and rear
pointers. I track the count of elements to distinguish between empty and full
states. For enQueue(), I add the value at rear and move rear forward using
modulo to wrap around. For deQueue(), I move front forward. The circular
nature is achieved by (index + 1) % k for advancing pointers. To get the rear
element, I use (rear - 1) % k since rear points to the next insertion
position. I use count to efficiently check isEmpty() and isFull() without
needing to track both pointers separately. This design achieves constant time
operations with fixed space.
O(1) time per operation, O(k) space
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
   


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()