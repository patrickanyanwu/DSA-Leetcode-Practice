"""In the case where there is no head.next (list size is 1) we check if n  is 1 (they want us to remove the head) if so we return None and if n is greater (out of bounds) we return the head.
Other cases we use an ahead pointer that goes ahead N times.
Used a count variable to record how many times ahead has moved,
if there is no ahead.next at any point we will check if we have done the correct amount of moves (n == count, basically it wants us to remove the first node) if so we return head.next to disconnect the first node.
Count increment is before the head.next for the case where ahead reaches the end.
We then move both the curr and ahead until we reach the end, afterward we set a rem variable to the node we want to remove, set a connect variable to the node we want our curr to connect to,
finally we set the curr node’s next to the connect node and we set the rem’s next to None to disconnect the node.
O(n) time O(1) space."""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = curr = head
        count = 0
        if head.next:
            for j in range(n):
                count += 1
                if ahead.next:
                    ahead = ahead.next
                else:
                    if n == count:
                        return head.next
                    else:
                        return head
            while ahead.next:
                curr = curr.next
                ahead = ahead.next
            rem = curr.next
            connect = curr.next.next
            curr.next = connect
            rem.next = None
        else:
            if n == 1:
                return None
        return head
