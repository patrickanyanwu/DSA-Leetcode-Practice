# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I used level-order traversal with a queue to
process the tree level by level. For each
level, I tracked the number of nodes and
their sum, then calculated the average by
dividing the sum by the count. I added
children to the queue for processing the
next level.
O(n) time O(w) space
"""

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            length = len(q)
            level_sum = 0
            for i in range(length):
                curr = q.popleft()
                level_sum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_sum / length)
        return res