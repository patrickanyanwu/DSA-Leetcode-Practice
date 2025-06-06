"""
  Run a 2 pointer sliding window aproach, 
  the window opens as we have an increasing sequence
  as soon as we dont we apppend the numbers at l and r and we move l up to r,
  If the numbers at l and r are equal we just append the number and if we are at the end of the array we have special cases for them.
  O(n) time O(n) space
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [f"{nums[0]}"]
        res = []
        l, r = 0, 1

        while r < len(nums):
            if nums[r - 1] + 1 == nums[r]:
                if r == len(nums) - 1:
                    res.append(f"{nums[l]}->{nums[r]}")
                r += 1
            else:
                if nums[l] == nums[r - 1]:
                    res.append(f"{nums[l]}")
                else:
                    res.append(f"{nums[l]}->{nums[r - 1]}")
                l = r
                if r == len(nums) - 1:
                    res.append(f"{nums[l]}")
                r += 1
        return res
