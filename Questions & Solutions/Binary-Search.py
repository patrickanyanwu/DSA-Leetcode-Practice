"""Set l at beginning of array and r at the end. As we start our loop we set a middle index being left pointer plus half of the distance between left and right,
this is done to ensure no overflow with large array sizes that could occur if i used (r + l) // 2.
I then check if the number at index m is equal to target, if so i return m, if it is less i increment my left pointer and if its greater i decrement my right pointer and loop continues while l <= r.
if there is no return of m (the number is not in the array) we return -1.
(O (log n) time when array is already sorted and O(n log n) time when array is not sorted as .sort() function is O(n log n) time) O(1) space always.
"""

"""When input array is sorted"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
"""When input array is not sorted"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
