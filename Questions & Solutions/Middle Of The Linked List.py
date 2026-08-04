"""
    We use slow and fast pointers,
    slow moves 1 at a time while fast moves 2 at a time.
    By the time the fast node hits the end of the list the
    slow pointer will be at the middle node.
    O(n) time O(1) space
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow