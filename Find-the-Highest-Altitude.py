"""
  Keep track of a max altitude and a current altitude,
  we then count our prefix sum troughout the array and keep track of the max altitude while traversing.
  Return max altitude.
  O(n) time O(1) space.
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAl = 0
        curAl = 0
        for g in gain:
            curAl += g
            maxAl = max(maxAl, curAl)
        return maxAl
