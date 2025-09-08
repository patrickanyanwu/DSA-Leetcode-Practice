"""
  Set a pointer to the next node,
  while the next node is equal to the currentnode
  we move the next node up
  after that is done we set current nodes next to be that node
  we do this iteratively while we have a next node to add.
  O(n) time O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        tail = head
        currnext = head.next
        while currnext:
            while currnext and head.val == currnext.val:
                delete = currnext
                currnext = currnext.next
                delete.next = None
            head.next = currnext
            head = head.next
        return tail
