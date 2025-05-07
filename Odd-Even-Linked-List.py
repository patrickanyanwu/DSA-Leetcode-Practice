"""
  We keep track of even indexed nodes with our even pointer and keep track of odd indexed nodes with our odd pointer.
  while we have not processed all nodes we set odd's next to even's next and said even's next to odd's next.
  This connects the odd and even indexed nodes independently,
  we then join them together by setting odd.next to evens head node.
  O(n) time O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return head
