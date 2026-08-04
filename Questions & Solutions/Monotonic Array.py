"""
I checked if the array is monotonic by tracking both increasing and
decreasing trends simultaneously. I initialize both flags to True and
iterate through the array comparing consecutive elements. If I find an
element smaller than the previous, the array can't be increasing, so I
set that flag to False. If I find an element larger than the previous,
it can't be decreasing, so I set that flag to False. An array is
monotonic if it's either entirely non-increasing or non-decreasing, so
I return True if at least one flag remains True.
O(n) time O(1) space
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            elif nums[i] > nums[i - 1]:
                decreasing = False
        return increasing or decreasing