"""In the case where the length of the array is 0 we return None, in the case where the length is 1 we check if the node is None if so we return None and if it is not None we return that head node.
Now we create a merge helper function that will merge all linked lists, this is made by creating a dummy node and updating its next with the lower value between the two lists nodes, we then return the head of the new list.
Now with our for loop we reassign the list at index i in our array to the list that was the result of merging the current and previous list so that in the next iteration it is merge sorting the next list with the previously merge sorted lists.
O(n * k) time and O(1) space"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            if lists[0] == None:
                return None
            else:
                return lists[0]
        elif len(lists) == 0:
            return None
        def merge(head1, head2):
            dummy = head = ListNode()
            while head1 and head2:
                if head1.val < head2.val:
                    dummy.next = head1
                    head1 = head1.next
                else:
                    dummy.next = head2
                    head2 = head2.next
                dummy = dummy.next
            dummy.next = head1 or head2
            return head.next
        for i in range(1, len(lists)):
            lists[i] = merge(lists[i - 1], lists[i])
        return lists[-1]
