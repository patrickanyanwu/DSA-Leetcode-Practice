"""
  We run a dfs and for each node we traverse we keep track of the max node in the path we took,
  if the current nodes value is greater than or equal to the maxnodes value we increment our count as it is a good node.
  O(n) time O(n) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def dfs(cur, maxval):
            if cur.val >= maxval:
                count[0] += 1
            if cur.left:
                dfs(cur.left, max(maxval, cur.val))
            if cur.right:
                dfs(cur.right, max(maxval, cur.val))
        dfs(root, root.val)
        return count[0]
