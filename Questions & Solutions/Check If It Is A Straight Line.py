"""
I checked if all points lie on the same line by verifying they all have the
same slope with the first two points. I calculate dx and dy from the first
two points to establish the reference slope. For each remaining point, I use
cross multiplication to check if the slope matches: (x - x1) * dy should
equal (y - y1) * dx. This avoids division and handles vertical lines (dx=0)
naturally. If any point has a different slope, the points don't form a
straight line. This cross-multiplication approach is more robust than
calculating slopes directly.
O(n) time O(1) space
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dx = x2 - x1
        dy = y2 - y1

        for x, y in coordinates[2:]:
            if (x - x1) * dy != (y - y1) * dx:
                return False

        return True