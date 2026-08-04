"""
  Use DFS to traverse the tree and calculate heights.
  At each node, the diameter passing through it is the sum of left subtree height + right subtree height.
  Track the maximum diameter globally using a nonlocal variable.
  The dfs function returns the height of the current subtree (1 + max of left/right heights) for its parent to use.
  Key insight: diameter doesn't have to pass through root, so we check at every node.
  O(n) time, O(h) space where h is tree height for recursion stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res