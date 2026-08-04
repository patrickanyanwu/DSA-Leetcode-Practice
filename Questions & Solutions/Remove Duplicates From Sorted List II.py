"""
    We have 2 pointers left and right which start off right next to each other,
    we will use these to compare values,
    initialize a dummy node to construct the ouput list
    if the values are not equal we add the left node to our output list.
    While the values are equal we move the right pointer up untill its not
    At the end of each iteration we set left to be right (ignores duplicates because of inner loop),
    and set the right to. be right.next.
    After the loop ends we set dummy.next to be left to cover cases where the final node was not a duplicate.
    O(n) time O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, head.next

        dummy = tail = ListNode()

        while right:
            if right.val != left.val:
                dummy.next = left
                dummy = dummy.next
            else:
                while right and right.val == left.val:
                    right = right.next
            left = right
            if right:
                right = right.next
        dummy.next = left
        return tail.next
