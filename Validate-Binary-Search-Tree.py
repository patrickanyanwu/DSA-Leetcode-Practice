"""We run recursive DFS and we have 2 bounds a left and right left < curr.val < right.
As we go left we know the node has to be less than its parent so we update our right bound and if we go right we update our left bound as the node needs to be greater than its parent. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(curr, left, right):
            if not curr:
                return True
            if not (curr.val > left and curr.val < right):
                return False
            return (traverse(curr.left, left, curr.val) and traverse(curr.right, curr.val, right))
        return traverse(root, float("-inf"), float("inf"))
