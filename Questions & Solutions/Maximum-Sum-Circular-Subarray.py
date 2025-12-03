class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        I used Kadane's algorithm twice to handle circular subarrays. I track
        both the maximum subarray sum (normal case) and minimum subarray sum.
        For the circular case, the maximum circular sum equals total sum minus
        the minimum subarray sum, since excluding the minimum middle section
        leaves the maximum wrapped-around section. I handle the edge case where
        all numbers are negative by checking if best_max is negative, returning
        it directly. Otherwise, I return the maximum of the normal case and the
        circular case to cover both scenarios.
        O(n) time O(1) space
        """
        total = sum(nums)

        cur_max = best_max = nums[0]
        cur_min = best_min = nums[0]

        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            best_max = max(best_max, cur_max)

            cur_min = min(num, cur_min + num)
            best_min = min(best_min, cur_min)

        if best_max < 0:
            return best_max

        return max(best_max, total - best_min)