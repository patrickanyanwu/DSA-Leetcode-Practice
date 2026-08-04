"""
  Use a hashmap with the key being the node in the original list and the value being the new copy of that node.
  We loop through the list populating the hashmap then we loop through the list from the head again,
  as we loop through we set the current node's copy's next to be the current node's next's copy.
  At the sae time we set the current node's copy's random to be the current node's random's copy.
  O(n) time O(n) space.
"""



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dic1 = {}
        curr = head
        while curr:
            dic1[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            dic1[curr].next = dic1.get(curr.next, None)
            dic1[curr].random = dic1.get(curr.random, None)
            curr = curr.next
        return dic1[head]
