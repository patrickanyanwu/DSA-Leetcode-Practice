# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I used DFS to flatten the tree in-place by
recursively processing left and right
subtrees, connecting the left subtree's
tail to the right subtree, and moving the
left subtree to the right position.
O(n) time O(h) space
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        def dfs(node):
            if not node:
                return None
            
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail or left_tail or node

        dfs(root)