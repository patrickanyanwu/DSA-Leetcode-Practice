"""
  Use a monotonic decreasing deque to track indices of potential maximum elements.
  The deque stores indices in decreasing order of their values.
  For each new element, remove smaller elements from the back (they can never be maximum).
  Remove indices outside the current window from the front.
  The front of the deque always contains the index of the maximum element in the current window.
  O(n) time, O(k) space.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output