"""
  Run dfs and after going left and right we then add the nodes value to the result.
  O(n) time O(n) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(curr):
            if curr.left:
                dfs(curr.left)
            if curr.right:
                dfs(curr.right)
            res.append(curr.val)
        dfs(root)
        return res
