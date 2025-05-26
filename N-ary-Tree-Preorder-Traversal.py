"""
  Add current node to result then traversal all its children depth first.
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []

        def dfs(curr):
            res.append(curr.val)
            for child in curr.children:
                dfs(child)
        dfs(root)
        return res
            
