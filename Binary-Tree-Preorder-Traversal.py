"""
  Run dfs and add nodes value to result before going left then right.
  O(n) time O(n) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(curr):
            res.append(curr.val)
            if curr.left:
                dfs(curr.left)
            if curr.right:
                dfs(curr.right)
        dfs(root)
        return res
