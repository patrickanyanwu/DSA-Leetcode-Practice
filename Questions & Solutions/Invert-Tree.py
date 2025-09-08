"""Recursively set the nodes left equal to its right, temp variable used to hold the left so that it reassigns correctly.
The base case is when the current node is none (we've hit the end of the tree) in that case we return none so the parent node still has no child in that position.
After each node has gone left and right we return that node so the reassignment works. 
O(n) time O(1) space."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverse(curr):
            if curr == None:
                return None
            temp = curr.left
            curr.left = inverse(curr.right)
            curr.right = inverse(temp)
            return curr
        root = inverse(root)
        return root
