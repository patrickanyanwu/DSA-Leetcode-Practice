"""
    I used a sliding window approach with two pointers to check for two adjacent increasing subarrays of length k. 
    I tracked consecutive positions where both the left and right windows showed increasing patterns, 
    counting valid pairs until I found k consecutive valid positions or exhausted the array.
    O(n) time O(1) space.
"""

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l = 0
        count = 1
        for r in range(k, len(nums) - 1):
            if count == k:
                return True
            if nums[l] < nums[l + 1] and nums[r] < nums[r + 1]:
                count += 1
            else:
                count = 1
            l += 1
        return count == k