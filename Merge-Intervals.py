"""
  First we sort the intervals by start time, we then set a pointer at the first interval and begin our loop from the second interval.
  First we check if the intervals i and ints[j] is non overlapping, if so we append it and move our i pointer up to the interval at j to be processed next.
  If they are overlapping we merge the interval i and the current interval in the loop and move forward with the loop so then we now check against the merged interval.
  at the end we append the interval i which is the final interval to be appended and then return res.
  O(n log n) time O(n) space.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        ints = sorted(intervals, key=lambda x: x[0])
        i = ints[0]
        res = []
        for j in range(1, len(ints)):
            if i[1] < ints[j][0]:
                res.append(i)
                i = ints[j]
            else:
                i = [min(i[0], ints[j][0]), max(i[1], ints[j][1])]
        res.append(i)
        return res
