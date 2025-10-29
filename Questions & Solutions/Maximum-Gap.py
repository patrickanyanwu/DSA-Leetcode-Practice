"""
I used bucket sort to find the maximum gap
in linear time. I divided the range into
buckets and tracked min/max in each bucket.
The maximum gap is between buckets, not
within them.
O(n) time O(n) space
"""

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_num, max_num = min(nums), max(nums)
        if min_num == max_num:
            return 0

        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        prev_max = min_num
        max_gap = 0
        for bmin, bmax in buckets:
            if bmin == float('inf'):
                continue
            max_gap = max(max_gap, bmin - prev_max)
            prev_max = bmax

        return max_gap