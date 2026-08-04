"""
    I used level-order traversal with a queue to
    process each level. I stored all nodes in
    each level and connected them by setting
    each node's next pointer to the following
    node in the level array.
    O(n) time O(n) space
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            level = []
            for i in range(n):
                curr = q.popleft()
                level.append(curr)
            
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
        return root