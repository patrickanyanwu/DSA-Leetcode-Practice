"""Used a slow and fast pointer as they will eventually both meet each other, if the fast pointer goes off the list (there is no cycle) we return False,
If the loop finished then we return True.
O(n) time O(1) space."""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
