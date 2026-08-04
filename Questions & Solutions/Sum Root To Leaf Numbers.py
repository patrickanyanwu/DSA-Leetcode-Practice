# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I used DFS to traverse all root-to-leaf
paths, building the number as a string by
concatenating node values. When reaching a
leaf node, I converted the complete path
string to an integer and added it to the
total sum.
O(n) time O(h) space
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        def dfs(curr_node, curr_number):
            nonlocal total
            number = str(curr_node.val)

            if curr_node.left:
                dfs(curr_node.left, curr_number + number)
            if curr_node.right:
                dfs(curr_node.right, curr_number + number)

            if not curr_node.left and not curr_node.right:
                total += int(curr_number + number)
        dfs(root, "")
        return total