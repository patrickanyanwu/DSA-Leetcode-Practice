"""
  For each iteration we keep track of a minproduct and maxproduct for the cases where we have negatives,
  we cheack each max and min agains the curr num * minprod and maxprod so far and we also check against the number itself because the number could be larger or smaller than both.
  Whenever we hit a 0 we reset out max and min prod to avoid constant multiplication of 0.
  We then return res.
  O(n) time O(1) space.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod = maxprod = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                minprod = maxprod = 1
                continue
            temp = num * maxprod
            maxprod = max(num * minprod, num * maxprod, num)
            minprod = min(num * minprod, temp, num)
            res = max(res, maxprod)
        return res
