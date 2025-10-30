"""
    I computed the running sum by maintaining a
    cumulative sum variable and updating each
    element in place with the running total as
    I traversed the array.
    O(n) time O(1) space
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            nums[i] = pre_sum
        return nums