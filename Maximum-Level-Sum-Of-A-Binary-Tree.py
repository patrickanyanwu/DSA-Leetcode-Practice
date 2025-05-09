"""
  We run a level order traversal on the tree while incrementing a level sum for each level,
  compare each level sum to a max level sum.
  O(n) time O(n) space.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs(cur):
            q = deque()
            q.append(cur)
            maxlevel = (1, cur.val)
            l = 1
            while q:
                level = 0
                length = len(q)
                for i in range(length):
                    c = q.popleft()
                    level += c.val
                    if c.left:
                        q.append(c.left)
                    if c.right:
                        q.append(c.right)
                if level > maxlevel[1]:
                    maxlevel = (l, level)
                l += 1
            return maxlevel[0]
        return bfs(root)
