"""
  Create set of both arrays and returned a list containing their differences with the set difference operator.
  O(n + m) time O(n + m) space
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
