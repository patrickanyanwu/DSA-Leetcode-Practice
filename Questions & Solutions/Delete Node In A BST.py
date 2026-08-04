"""
  We recursively check for the node we want to remove, then we check if it has leaf nodes if it only has one i return the node we want to delete's leaf node.
  If it has 2 leaf nodes i find the minimum on the right subtree and replace the node we want to removed's value with that minimum node, we then delete that minimum node.
  O(n) time O(n) space.
"""

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_larger_node = self.getMin(root.right)

            root.val = min_larger_node.val
            
            root.right = self.deleteNode(root.right, min_larger_node.val)
        
        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node
