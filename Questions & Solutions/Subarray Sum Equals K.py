"""
I counted subarrays with sum k using prefix sums and a hash map. I maintain a
running sum and store the frequency of each prefix sum encountered. For each
position, I check if (curSum - k) exists in the map, meaning there are
subarray(s) ending at this position with sum k. I add the count of such
occurrences to the result. Then I update the frequency of the current prefix
sum. I initialize the map with {0: 1} to handle subarrays starting from index
0. Unlike the max length problem, I need all occurrences of each prefix sum
since multiple subarrays can have the same sum. This counts all valid
subarrays efficiently.
O(n) time O(n) space
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        curSum = res = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefix.get(diff, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)
        return res