"""
  Run dfs preorder while keeping track of a sum,
  if we hit a leaf node and the sum ever equals to the target we return and set res to be true.
  O(n) time O(log n) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = [False]
        def dfs(curr, summ):
            if curr.left:
                dfs(curr.left, summ + curr.val)
            if curr.right:
                dfs(curr.right, summ + curr.val)
            if not curr.left and not curr.right:
                if summ + curr.val == targetSum:
                    res[0] = True
        dfs(root, 0)
        return res[0]
