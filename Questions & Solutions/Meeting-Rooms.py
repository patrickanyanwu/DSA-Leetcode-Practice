"""
  First we sort the intervals be start time so we can make our checks accordingly,
  Now we check from the second interval and if the current intervals start time is less than the previous intervals end time,
  we know its overlapping and return false
  If not we continue to next iteration
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
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        ints = sorted(intervals, key=lambda x: x.start)
        for j in range(1, len(intervals)):
            if ints[j - 1].end <= ints[j].start:
                continue
            else:
                return False
        return True
