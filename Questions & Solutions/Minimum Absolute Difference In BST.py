# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I used inorder traversal to visit BST nodes
in sorted order. I tracked the previous node
value and calculated the difference with the
current node at each step. Since inorder
gives sorted values, the minimum difference
must be between consecutive nodes, so I
updated the minimum as I traversed.
O(n) time O(h) space
"""

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev = None

        def inorder(node):
            nonlocal min_diff, prev
            if not node:
                return

            inorder(node.left)

            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val

            inorder(node.right)

        inorder(root)
        return min_diff