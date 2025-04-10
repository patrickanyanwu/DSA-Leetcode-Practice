"""
  We start by making 2 arrays, one for start times sorted and another for end times sorted,
  we now have 2 pointers on both arrays, as we loop through we count how many meetings are currently happening and we increase a count and mover our start pointer up
  If we hit the end of a meeting we decrement our count and move our end time pointer up.
  We keep track of a maxcount to essentially return the max amount of meetings that were going on at the same time.
  O(n log n) time O(n) space.
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s = e = 0
        maxcount = 0
        count = 0
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            maxcount = max(maxcount, count)
        return maxcount
