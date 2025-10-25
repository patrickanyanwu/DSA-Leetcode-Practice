"""
    Firstly we make the linked list into a doubly linked list,
    we then have a variable pointing to the end of the linked list,
    now we loop over half of the linked list and compare values 1 by one.
    O(n) time O(1) space
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = curr = head
        length = 1
        while curr.next:
            curr.next.prev = curr
            curr = curr.next
            length += 1
        tail = curr
        
        for i in range(length // 2):
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.prev

        return True