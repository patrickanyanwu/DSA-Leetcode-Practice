"""
  Use a monotonic increasing stack to track (index, height) pairs.
  For each bar, if it's shorter than the top of the stack, we found the right boundary for previous bars.
  Pop taller bars and calculate their max rectangle area using (current_index - bar_start_index) as width.
  Key insight: when popping, we keep the index from the popped element since that bar can extend left to where smaller bars were.
  After the loop, process remaining bars in stack using the full remaining width to the end.
  O(n) time, O(n) space.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0
        for i, height in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                res = max(res, h * (i - idx))
            stack.append((idx, height))

        while stack:
            idx, h = stack.pop()
            res = max(res, h * (n - idx))
        return res