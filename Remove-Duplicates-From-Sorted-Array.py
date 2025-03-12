"""Use 2 pointers, l which stays at the next swapping index and r which loops through array one by one, count is used to keep track of how many duplicates weve seen.
While we have a duplicate number we increment r,
once we find an non duplicate or we go out of bounds we check the minimum between our count and 2 because we want to do at most 2 swaps to maintain integrity.
While swapping we increment l so we keep at the next swapping position at all times.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0

        while r < len(nums):
            count = 1
            while r < len(nums) - 1 and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
