"""
    I used the Dutch National Flag algorithm
    with three pointers. I moved 0s to the left,
    2s to the right, and left 1s in the middle
    by swapping elements as I traversed through
    the array once.
    O(n) time O(1) space
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1