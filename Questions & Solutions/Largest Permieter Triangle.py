"""
    Sort the array then loop backwards and check every consecutive triplet,
    whenever we find one that can form a triangle we return that permimeter,
    we loop backwards gto make sure we find the largest first.
    O(n log n) time O(1) space.
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()


        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0