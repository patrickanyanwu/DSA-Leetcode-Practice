"""
I added two numbers represented as linked lists where digits are stored
in non-reversed order. Since the most significant digit is first but
addition starts from the least significant digit, I reverse both lists
first. Then I perform standard addition with carry, iterating while
either list has nodes or there's a carry remaining. For each position,
I sum the values (or 0 if list is exhausted) plus carry, compute the
new digit and carry, and build the result list. Finally, I reverse the
result list to restore the correct order before returning.
O(max(n, m)) time O(1) space excluding output
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            before = None
            cur = head
            after = cur

            while after:
                after = cur.next
                cur.next = before
                before = cur
                cur = after
            return before
            
        l1 = reverseList(l1)
        l2 = reverseList(l2)

        tail = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            dummy.next = ListNode(val)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return reverseList(tail.next)

