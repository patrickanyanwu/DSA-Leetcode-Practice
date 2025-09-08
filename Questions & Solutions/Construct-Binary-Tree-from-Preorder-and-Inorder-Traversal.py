"""We know to root of the current subtree is the first node in the preorder list, so then we get what index that node has in the inorder traversal,
this tells us how many nodes we need to construct the left and right subtrees.
For the left we need everything in preorder from 1 up until and including the node at index mid as the mid index in inorder tells us how many nodes to the right of the current root do we need to make the left subtree.
We then use everything in inorder up until the mid index. We do the opposite for the right subtrees.
O(n^2) time, O(n) space."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
