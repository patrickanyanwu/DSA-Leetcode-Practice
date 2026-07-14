"""
Process people from right to left using a monotonic decreasing stack of heights.
For each person, pop everyone shorter from the stack — each pop is someone this person can see over.
If the stack still has someone left after popping, that person is taller (or equal) and blocks the view, but is still visible, so count them too.
Push the current person's height onto the stack before moving left.
O(n) time since each person is pushed and popped at most once, O(n) space for the stack and result array.
"""

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []  # monotonic non-increasing stack of heights

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                res[i] += 1
            if stack:  # there's a taller (or equal) person blocking further view
                res[i] += 1
            stack.append(heights[i])

        return res