"""
I sorted the array and used three pointers
to find the closest sum. For each fixed
element, I used two pointers to find the
best pair, tracking the smallest difference
from the target throughout.
O(n^2) time O(1) space
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = (float("inf"), 0)
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                diff = abs(target - threeSum)
                if res[0] > diff:
                    res = (diff, threeSum)
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return target
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res[1]