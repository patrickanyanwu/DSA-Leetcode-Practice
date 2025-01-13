"""We set a before pointer equal to none, set a temp variable equal to the lists head and a after variable also equal to the lists head.
Now our loop runs while we have an after node, we set after = to its next,
set temp’s next = to the before node then we update before by moving it to temp and we set temp equal to after In order to move temp over to the next node and continue our loop. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        temp = head
        after = head
        while after:
            after = after.next
            temp.next = before
            before = temp
            temp = after
        return before
