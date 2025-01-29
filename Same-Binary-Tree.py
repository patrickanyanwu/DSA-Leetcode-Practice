"""Used BFS to collect the values of each tree, output will check if the values are equal.
Used a queue for the BFS as it allows for O(1) popleft.
How my BFS works is the current node gets popped from the queue and it adds the current nodes children to the queue so then in following iterations it adds each nodes children.
When the current node gets popped from the queue its value is added to the values array. But if we have a left exclusively or a right we append None to the queue,
we do this to keep track of when a node has only one child so in the case where the 2 trees have the same values but the tree has a certain value in a different position than that value in the other tree
e.g (node has 4 on the left, but on other tree it has 4 on the right it is not the same tree). 
O(n) time, O(1) space."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def BFS(curr):
            queue = deque()
            queue.append(curr)
            values = []
            while queue:
                current_node = queue.popleft()
                if current_node == None:
                    values.append(None)
                    continue
                values.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right and not current_node.left:
                    queue.append(None)
                if current_node.left and not current_node.right:
                    queue.append(None)
                if current_node.right:
                    queue.append(current_node.right)
            return values
                
        return BFS(p) == BFS(q)
