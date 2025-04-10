"""
  For each iteration we check if the current intervals start time is greater than the newintervals end time,
  or if the current intervals end time is less than the newintervals start time.
  In the first case we know that we should append the new interval then return the rest of the array.
  In the second case we just append the current interval as we have not found the place for the new interval yet.
  If neither of these are true we have an overal so we set the newinterval to the merged interval between the current and new interval and move forward in that way.
  If we end up mergeing up untill the end of the array we just append the new interval and return res.

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
