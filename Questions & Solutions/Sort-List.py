# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        I implemented merge sort on a linked list to achieve O(n log n) sorting.
        I use a slow/fast pointer approach to find the middle node, which splits
        the list in half. The find_mid function returns the node before the
        midpoint so I can properly disconnect the two halves. I recursively sort
        each half until I reach base cases of single nodes or empty lists. Then
        I merge the sorted halves by comparing values and linking nodes in order.
        This divide-and-conquer approach efficiently sorts the list in place
        without using extra space for arrays.
        O(n log n) time O(log n) space
        """
        def find_mid(curr):
            slow = curr
            pre = None
            fast = curr
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            return pre
        def merge(list1, list2):
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
        def merge_sort(curr):
            if not curr or not curr.next:
                return curr
            mid = find_mid(curr)
            tmp = mid.next
            mid.next = None
            left = merge_sort(curr)
            right = merge_sort(tmp)
            return merge(left, right)

        return merge_sort(head)