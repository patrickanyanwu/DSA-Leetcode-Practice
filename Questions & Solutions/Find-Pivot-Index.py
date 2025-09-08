"""
  We get the entire sum of the nums array then we keep track of a prefix sum,
  as we iterate we check if the current prefix sum is equal to the full sum - our prefixsum - the current number (the suffix sum).
  O(n) time O(1) space.
"""

class Solution:
    def pivotIndex(self, nums):
        sum1 = sum(nums)
        presum = 0
        for i, num in enumerate(nums):
            if presum == (sum1 - presum - num):
                return i
            presum += num
        return -1
