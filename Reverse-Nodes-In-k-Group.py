"""
  Our essential logic here is on each iteration of the while loop we first check if we have K elements left to reverse,
  if we do we hold the start of the list we are about to reverese,
  we then reverse the next k elements of the list and set the start of the current reveresed group's next to be the next part of the list that needs to be reversed,
  and also set the previously reversed side of the lists next to be the new start of the group of the list we just reversed.
  O(n) time O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next 

            group_start = prev_group.next
            next_group = kth.next

            prev, curr = None, group_start
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            prev_group.next = prev
            group_start.next = next_group

            prev_group = group_start
