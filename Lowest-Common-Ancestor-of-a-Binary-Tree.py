"""for each node we check if the 2 nodes were trying to find’s values are greater than the current node, if it is then we know we need to check the right side, same goes for if values are less we have to go left.
If at any point the current nodes value is equal to p or q we return that node as it has to be the lowest ancestor.
If the current nodes value is greater than one of the p, q nodes and less than the other then we have found the lowest common ancestor and we return that node. 
O(log n) time O(1) space"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
