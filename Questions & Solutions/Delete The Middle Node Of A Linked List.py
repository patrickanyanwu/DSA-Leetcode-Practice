"""
  We first find the middle node using slow and fast pointers.
  After that we loop from the head until we find the node previous to the middle node,
  after found we set that nodes next to be the middle nodes next then set the middle nodes next to None to remove it from memory.
  O(n) time O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = head
        while cur and cur.next != slow:
            cur = cur.next
        cur.next = slow.next
        slow.next = None
        return head
