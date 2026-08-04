"""
  As we traverse the tree with dfs we use booleans to find the LCA,
  if we find one node in the left of a tree and we find one node in the right of a tree or
  the current node is one of the nodes we need to find and we find the other node in the left or right,
  we set the LCA to the current node.
  O(n) time O(n) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [0]

        def dfs(cur):
            if not cur:
                return False
            mid = False
            if cur == p or cur == q:
                mid = True
            left = dfs(cur.left)
            right = dfs(cur.right)
            if left + right + mid >= 2:
                res[0] = cur
            return left or mid or right
        dfs(root)
        return res[0]
