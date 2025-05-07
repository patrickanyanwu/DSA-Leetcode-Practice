"""
  Run dfs preorder on both trees while only appending leaf nodes values to an arrray.
  We then return true if both value arrays are equal.
  O(n + m) time O(n + m) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        def dfs1(cur):
            if cur.left:
                dfs1(cur.left)
            if cur.right:
                dfs1(cur.right)
            if not cur.right and not cur.left:
                res1.append(cur.val)
        dfs1(root1)
        res2 = []
        def dfs2(cur):
            if cur.left:
                dfs2(cur.left)
            if cur.right:
                dfs2(cur.right)
            if not cur.right and not cur.left:
                res2.append(cur.val)
        dfs2(root2)
        return res1 == res2
