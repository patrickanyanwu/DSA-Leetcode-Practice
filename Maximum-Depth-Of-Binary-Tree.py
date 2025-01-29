"""Run DFS and increment a count variable for every recursive call,
if we have hit a leaf node (the current node has no left or right) we calculate our max and we decrement our count so that the next node to traverse can find a new max if there is.
We manipulate our count and max count variables by using nonlocal (allows us to modify a variable outside of the function call). O(n) time O(1) space."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        count = 0
        maxCount = 0

        def traverse(curr):
            nonlocal count, maxCount  # Use nonlocal to modify outer function variables
            
            count += 1  # Increment depth when visiting a node
            
            if not curr.left and not curr.right:  # If it's a leaf node
                maxCount = max(maxCount, count)  # Update max depth
            
            if curr.left:
                traverse(curr.left)
            if curr.right:
                traverse(curr.right)
            
            count -= 1  # Decrement depth when backtracking

        traverse(root)
        return maxCount
