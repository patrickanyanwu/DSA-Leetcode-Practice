"""Use a slow and fast pointer to find the middle of the linked list.
We then disconnect the middle nodes next from the rest of the list and we reverse the second half of the list.
After we reverse we merge the first half of the list with the reversed second half of the list.
O(n) time O(1) space"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
