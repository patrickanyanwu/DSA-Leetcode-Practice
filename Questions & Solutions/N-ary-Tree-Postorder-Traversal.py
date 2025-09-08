"""
  Traversal all current nodes children then add the current nodes value to the result.
  O(n) time O(n) space
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []

        def dfs(curr):
            for child in curr.children:
                dfs(child)
            res.append(curr.val)
        dfs(root)
        return res
