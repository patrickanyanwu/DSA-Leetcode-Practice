"""
I found the maximum length subarray with sum k using prefix sums and a hash
map. I maintain a running sum and store the first occurrence of each prefix
sum with its index. For each position, I check if (curSum - k) exists in the
map, which means there's a subarray ending at current position with sum k. The
length is i - prefix[curSum - k]. I only store the first occurrence of each
prefix sum to maximize subarray length. I initialize the map with {0: -1} to
handle subarrays starting from index 0. This approach finds the longest
subarray efficiently in one pass.
O(n) time O(n) space
"""

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = {0: -1}
        curSum = 0
        res = 0

        for i, num in enumerate(nums):
            curSum += num

            if curSum - k in prefix:
                res = max(res, i - prefix[curSum - k])

            if curSum not in prefix:
                prefix[curSum] = i

        return res
