# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I performed level-order traversal using a
queue for tree nodes and a deque for each
level. I tracked direction with a boolean
flag that toggles each level. For left-to-
right levels, I appended values normally;
for right-to-left, I prepended them using
appendleft to build the reversed order
efficiently without extra reversal steps.
O(n) time O(w) space
"""
    
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        right = True
        while q:
            level = deque()
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                if right:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(list(level))
            right = not right
        return res