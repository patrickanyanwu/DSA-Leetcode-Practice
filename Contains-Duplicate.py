"""Thought Process:
Use set to add numbers in the array, check if a number is already in the set, and return True if so. O(n) time O(n) space
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in nums:
            if i in set1:
                return True
            set1.add(i)
        return False
