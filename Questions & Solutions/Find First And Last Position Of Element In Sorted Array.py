"""
I used binary search twice to find the first
and last positions of the target. For the
left bound, I continued searching left after
finding the target, and for the right bound,
I continued searching right.
O(log n) time O(1) space
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isLeft: bool) -> int:
            l, r = 0, len(nums) - 1
            bound = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    bound = mid
                    if isLeft:
                        r = mid - 1
                    else:
                        l = mid + 1
            return bound

        left = findBound(True)
        right = findBound(False)
        return [left, right]