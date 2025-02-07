"""We run BFS with a little twist, we add the root to the queue first as usual, now we get the length of the queue and create a level list.
Now, we clear each node in the queue before going to the next level.
So the root gets added to the level, and its children are added to the queue for our next level,
we add all nodes in the queue to the level list while at the same time we add their children to the queue for the next level.
This gives us a level ordere traversal. O(n) time O(n) space:"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                res.append(level)
        return res
