"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

I used level-order traversal with a queue to
process each level of the tree. For each
level, I connected nodes by setting the next
pointer from the previous node to the
current node, while adding children to the
queue for the next level.
O(n) time O(n) space
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                curr = q.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root