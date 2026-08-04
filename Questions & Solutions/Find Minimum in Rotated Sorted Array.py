"""We start our minimum at the first value in the array incase it is sorted.
Use binary search but if value at m is greater than or equal to value on the far left we put l = m + 1 to look at the lower values that haven’t been pivoted as pivoted values are on the left,
if not we put r = m – 1, if at any point the number at l is less than the number at r (the window is sorted) we return that number."""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        target = nums[0]
        l, r = 0, len(nums) - 1
        if len(nums) == 0:
            return None
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[r] > nums[l]:
                target = min(nums[l], target)
                break
            if nums[m] < target:
                target = nums[m]
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return target
