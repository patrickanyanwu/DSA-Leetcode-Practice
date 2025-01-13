"""We make a dummy node in order to create a new linked list which works by setting its next equal to the other lists nodes etc.
We also keep a tail pointer at the beginning of the new linked list so when we return our new list we return our tails next node.
Loop runs while we still have nodes to compare to in both lists. Now we compare values, if one head is lower than the other we set the dummy’s next equal to that node and we update that node to its next.
After the checks we set dummy equal to dummy’s next so we move through our linked list.
After that loop we set dummy equal to whatever list still has nodes in order to connect to the remaining nodes. Returned tail.next

O(n) time and O(1) space"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next 
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return tail.next
