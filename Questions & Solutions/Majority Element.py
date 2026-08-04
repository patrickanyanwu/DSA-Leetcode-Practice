"""have a result variable which holds our current most frequent number, we then loop through array and if the current number is the res number we increment our count.
If not we decrement our count but if the count is 0 which means that we have seen this current number more times than we have seen the res number, we set res equal to that number,
then set our count back to 1. This works as our count manipulations always gives us the most frequents element in the array as we loop through.
O(n) time O(1) space."""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for num in nums:
            if num == res:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    res = num
                    count = 1
        return res
