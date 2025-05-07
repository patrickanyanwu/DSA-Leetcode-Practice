"""
  Firstly we find the middle node of the list,
  we then reverse the second half of the list and set 2 pointers,
  left pointer at the beginning of the list and a right pointer at the beginning of the reversed second half of the list.
  We then check all sums and keep track of a max.
  O(n) time O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxsum = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        before = None
        cur = slow
        after = cur
        while after:
            after = cur.next
            cur.next = before
            before = cur
            cur = after
        left = head
        right = before
        while left.next:
            maxsum = max(maxsum, left.val + right.val)
            left = left.next
            right = right.next
        return maxsum
