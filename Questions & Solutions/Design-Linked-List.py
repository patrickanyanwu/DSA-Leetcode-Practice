"""
I implemented a singly linked list with a dummy head node to simplify edge
cases. The dummy node always points to the actual head, eliminating special
handling for empty lists. I track the size for efficient bounds checking. For
get(), I traverse to the index and return the value. For addAtHead() and
addAtTail(), I delegate to addAtIndex() with appropriate indices. For
addAtIndex(), I find the node before the insertion point and insert the new
node. For deleteAtIndex(), I find the node before deletion and skip over the
target node. Using a dummy head makes insertions and deletions uniform without
special cases for the head position.
O(n) time for operations (O(1) for head insertions), O(n) space
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy = Node() 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        prev.next = Node(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1
