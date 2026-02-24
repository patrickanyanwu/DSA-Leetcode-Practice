"""
  Use DFS to traverse the tree and check balance at each node.
  Each node returns a pair: [is_balanced, height].
  A tree is balanced if: left subtree is balanced AND right subtree is balanced AND height difference <= 1.
  Return the height as 1 + max(left height, right height) for parent nodes to use.
  Base case: empty node returns [True, 0].
  O(n) time, O(h) space where h is tree height for recursion stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]