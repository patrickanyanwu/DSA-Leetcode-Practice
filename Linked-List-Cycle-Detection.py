"""Used a hash set to store the nodes and if a node was already in the set I returned true.
If the loop ended I returned false.
O(n) time O(n) space"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set1 = set()
        while head:
            if head not in set1:
                set1.add(head)
                head = head.next
            else:
                return True
        return False
