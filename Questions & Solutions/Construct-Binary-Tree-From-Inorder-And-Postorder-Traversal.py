# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I used a hash map to quickly find where each
value appears in the inorder traversal,
which helps me split the tree into left and
right subtrees. Since postorder visits nodes
in the order left-right-root, I process it
backwards (right to left) to build the tree
from the root down. For each root value from
postorder, I find its position in inorder,
which tells me what elements belong to the
left subtree (everything before that
position) and right subtree (everything
after). I recursively build the right
subtree first, then the left subtree,
because I'm processing postorder in reverse.
O(n) time O(n) space
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        self.post_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            mid = idx_map[root_val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root
        
        return build(0, len(inorder) - 1)