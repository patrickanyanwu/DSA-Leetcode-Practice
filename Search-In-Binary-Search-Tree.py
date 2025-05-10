"""
  Run a BFS and if the nodes val corresponds to the target i return that node.
  O(n) time O(n) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur.val == val:
                return cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return None
