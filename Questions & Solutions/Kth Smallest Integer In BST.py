"""We run DFS inOrder and every time we append to our results list we check if the length of our result is equal to k and if so we stop the recursion.
We then return res at k – 1.
O(n) time O(n) space"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def traverse(curr):
            if curr.left:
                traverse(curr.left)
            res.append(curr.val)
            if len(res) == k:
                return
            if curr.right:
                traverse(curr.right)
        traverse(root)
        return res[k - 1]
