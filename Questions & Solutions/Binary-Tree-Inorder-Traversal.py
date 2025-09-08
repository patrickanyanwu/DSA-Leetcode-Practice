"""
  Run a dfs and after going to thr current nodes left we add the nodes value to the result then traverse right.
  O(n) time O(n) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(curr):
            if curr.left:
                dfs(curr.left)
            res.append(curr.val)
            if curr.right:
                dfs(curr.right)
        dfs(root)
        return res
