# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        I used recursion to build a height-balanced BST from a sorted array.
        The key insight is that the middle element becomes the root to ensure
        balance. I find the midpoint, create a node with that value, then
        recursively build the left subtree from the left half and the right
        subtree from the right half. The base case is when the array is empty,
        returning None. Since the array is already sorted, this approach
        guarantees a balanced tree with minimal height.
        O(n) time O(log n) space
        """
        if not nums:
            return None

        midindex = len(nums) // 2
        mid = nums[midindex]

        root = TreeNode(mid)

        root.left = self.sortedArrayToBST(nums[:midindex])
        root.right = self.sortedArrayToBST(nums[midindex + 1:])
        return root