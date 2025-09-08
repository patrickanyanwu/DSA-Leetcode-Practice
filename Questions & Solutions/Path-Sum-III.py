"""
  Keep track of prefix sums in a hashmap and a current sum from the root in our dfs,
  if our curentsum - target is in our prefix sum hashmap that means there exists some currentsum - prefixsum = target,
  so we increment our result by the amount of times that prefixsum has occured.
  O(n) time O(n) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_count = {0: 1}
        result = 0
        
        def dfs(node, current_sum):
            nonlocal result
            if not node:
                return
            
            current_sum += node.val

            result += prefix_sum_count.get(current_sum - targetSum, 0)
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            prefix_sum_count[current_sum] -= 1

        dfs(root, 0)
        return result
