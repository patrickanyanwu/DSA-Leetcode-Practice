"""Thought Process:
We check if the set of nums is a different size to the original nums array, if its not that means there is a duplicate as sets remove duplicates.
O(n) time O(n) space
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
