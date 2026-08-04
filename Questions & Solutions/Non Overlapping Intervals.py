"""
  Sort intervals be end time and set a pointer at the first interval,
  We loop starting from 1 onwards and if we find an overlap we increment our count,
  If the current 2 dont overlap we move i up to that current at j.
  This is so we keep track of how many we need to merge for that specific interval at i before we then process the rest.
  O(n log n) time O(n) space.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        ints = sorted(intervals, key=lambda x: x[1])
        i = ints[0]
        count = 0
        for j in range(1, len(ints)):
            if i[1] <= ints[j][0]:
                i = ints[j]
            else:
                count += 1
        return count
