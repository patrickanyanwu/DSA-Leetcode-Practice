"""
  Run dfs while keeping track of our depth and directions.
  If our direction is left we run dfs on the left subtree and change the direction to the right and vice versa.
  For each step we either go the intended direction and increment our step or we go the other direction and reset the steps to 1 to find another path.
  O(n) time O(n) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        count = [0]
        def dfs(root, direction, steps):
            if direction == "right":
                if root.right:
                    dfs(root.right, "left", steps + 1)
                if root.left:
                    dfs(root.left, "right", 1)
            elif direction == "left":
                if root.left:
                    dfs(root.left, "right", steps + 1)
                if root.right:
                    dfs(root.right, "left", 1)
            count[0] = max(count[0], steps)
        dfs(root, "left", 0)
        dfs(root, "right", 0)
        return count[0]
