"""
First, I handled edge cases, such as an empty list, a single-node list, or when no rotation is needed (`k == 0`). 
Then, I calculated the length of the list (`count`) and determined the effective number of rotations (`r = k % count`) to avoid unnecessary full-circle rotations. 
I identified the new head of the rotated list by traversing to the appropriate node, 
adjusted the pointers to break and reconnect the list, and finally returned the new head.
O(n) time O(1) space.
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        if not head.next:
            return head
        cur = head
        tail = None
        count = 0
        while cur:
            count += 1
            if not cur.next:
                tail = cur
            cur = cur.next
        r = k % count
        cur = head
        for i in range(count - r - 1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        tail.next = head if newhead else None
        return newhead or head
