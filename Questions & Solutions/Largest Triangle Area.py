"""
    We keep track of a gloabal max
    We check for all possible compinations of 3's
    if the area is greater than our global max
    and update accordingly.
    O(n ^ 3) time O(1) space
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangle_area(x1, y1, x2, y2, x3, y3):
            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

        max_area = 0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            area = triangle_area(x1, y1, x2, y2, x3, y3)
            max_area = max(max_area, area)
        return max_area