"""
    We make a dummy node which will reconstruct the new list,
    we then loop through the list and add every node that isnt equal to the val to our new list
    after we add any node we set that nodes next to be none to safely remove it from the list
    to avoid adding more than 1 element to the new list
    O(n) time O(1) space
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tail = dummy = ListNode()

        curr = head
        while curr:
            if curr.val != val:
                dummy.next = curr
                dummy = dummy.next
            tmp = curr
            curr = curr.next
            tmp.next = None
        return tail.next