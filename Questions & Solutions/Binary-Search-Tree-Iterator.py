# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I implemented an iterator for BST inorder
traversal using a stack. I initialize by
pushing all left nodes from root onto the
stack. For next(), I pop the top node,
return its value, then push all left nodes
of its right child. This simulates inorder
traversal iteratively, visiting nodes in
sorted order without precomputing all
values.
O(1) next/hasNext amortized, O(h) space
"""

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()