"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        I used recursion to build a quad tree from a 2D grid. For each region,
        I first check if all values are uniform by comparing every cell to the
        first value. If uniform, I create a leaf node with that value. If not
        uniform, I divide the region into four quadrants and recursively build
        each quadrant. I split by halving the size and adjusting row/column
        offsets for top-left, top-right, bottom-left, and bottom-right. The
        base case is when a region is uniform, creating a leaf. This divides
        the grid hierarchically until all regions are uniform.
        O(n²) time O(n²) space
        """

        def build(r0, c0, size):
            first = grid[r0][c0]
            uniform = True
            for r in range(r0, r0 + size):
                if not uniform:
                    break
                for c in range(c0, c0 + size):
                    if grid[r][c] != first:
                        uniform = False
                        break
            
            if uniform:
                return Node(first == 1, True, None, None, None, None)

            half = size // 2
            
            return Node(
                True,  
                False,
                build(r0, c0, half),                     # top-left
                build(r0, c0 + half, half),              # top-right
                build(r0 + half, c0, half),              # bottom-left
                build(r0 + half, c0 + half, half)        # bottom-right
            )

        return build(0, 0, len(grid))