"""We loop through the array and add the product of everything before each number into our result array, we update our prefix by multiplying it by our current number afterwards.
We then loop backwards through the array and multiply our prefix by our postfix (product of everything after) and then update our postfix.
O(n) time O(n) space"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
