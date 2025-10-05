"""
  Make 2 heads, 1 for every node < x and the other for all nodes >= x.
  We first store the next node in a variable then safely detatch it from the original list
  As we loop through the list we attatch the node to the appropriate list.
  After the loop we set the before lists heads next to be the after lists head and return the before lists head
  O(n) time O(1) space.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = before = ListNode()
        after_head = after = ListNode()
        
        while head:
            nxt = head.next
            head.next = None 
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = nxt
        
        before.next = after_head.next
        return before_head.next
