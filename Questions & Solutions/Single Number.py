"""
  Use the xorr operator over each number in the array and whichever number that only shows up once will be the result of the xorring.
  Xorring a number by itself is 0, and 0 xorr any number is that number so it will end up being 0 xorr the single number which will give us the single number.
  O(n) time O(1) space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr = nums[0]
        for i in range(1, len(nums)):
            xorr ^= nums[i]
        return xorr
