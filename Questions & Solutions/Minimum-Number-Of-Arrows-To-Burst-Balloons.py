"""
  We sort the points by the end point,
  now we start our count at 1 and any time we find a non overlapping interval we increment our count
  and update our current end were looking at.
  While we overlapping intervals with a singular point we know we can pop all of those ballons with 1 arrow
  as its start dimension is less than or equal to that singular points end dimension.
  O(n log n) time o(1) space
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        count = 1
        points.sort(key=lambda x: x[1])
        currend = points[0][1]
        for i in range(1, len(points)):
            x, y = points[i]
            if x > currend:
                currend = points[i][1]
                count += 1
        return count
