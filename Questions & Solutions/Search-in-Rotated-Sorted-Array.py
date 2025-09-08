"""Use binary search then we check if were in the rotated area on the left (nums[m] >= nums[l]) or the non rotated area on the right.
If we are in the rotated part we check if our target is less than the number on the far left or if our target is greater than nums[m] if one or the other is true we need to move to the right.
if not (when target is greater than left and less than right) we move to the left. 
In the case where we are in the right side (non pivoted area) we check if target is greater than the number on the far right or less than the nums[m] in that case we move to the left.
If not we move to the right.

O(log n) time and O(1) space.
"""



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
