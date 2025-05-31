"""
  Use a sliding window algorithm, as we inrcrement our cursum with an r pointer we check if the cursum is >= target
  if it is we check its length and decrement our cursum and increment our left pointer to close our window.
  o(n) time O(1) space
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        cursum = 0
        minlength = float("inf")
        
        for r in range(n):
            cursum += nums[r]
            
            while cursum >= target:
                minlength = min(minlength, r - l + 1)
                cursum -= nums[l]
                l += 1
        
        return 0 if minlength == float("inf") else minlength
