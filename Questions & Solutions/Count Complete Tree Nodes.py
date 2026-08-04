# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I leveraged the complete tree property to
optimize counting. I compared the leftmost
and rightmost heights at each node. If
they're equal, the subtree is perfect, so I
used the formula 2^h - 1 to count nodes
instantly. Otherwise, I recursively counted
left and right subtrees. This avoids
visiting every node by exploiting the tree's
structure.
O(log^2 n) time O(log n) space
"""

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        left_h = left_height(root)
        right_h = right_height(root)

        # If equal: perfect tree
        if left_h == right_h:
            return (1 << left_h) - 1

        # Otherwise: recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)