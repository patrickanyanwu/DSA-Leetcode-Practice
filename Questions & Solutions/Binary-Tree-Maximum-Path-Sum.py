"""For each node in the tree we recursively get the max sum if we were to go left and if we were to go right in the tree,
if at any point a node is negative we return 0 to our sum.
For a sum to be allowed it has to only split once so when we make our left and right checks we check if we were to add the current node to both the left and right maxes would the sum be greater than our max,
]if do we update our max and continue the recursion.
O(n) time O(n) space (due to the call stack)."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(curr):
            if not curr:
                return 0
            leftMax = max(dfs(curr.left), 0)
            rightMax = max(dfs(curr.right), 0)

            res[0] = max(res[0], curr.val + leftMax + rightMax)
            return curr.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
