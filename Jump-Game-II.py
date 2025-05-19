"""
  Greedy.
  Current_end holds the farthest index we can reach in our current jump,
  farthest holds the farthest index we can reach given the values weve seen so far,
  as soon as we reach our current end we increment our jumps and set our next farthest we can reach in the jump
  to be the farthest we have seen so far (farthest variable).
  O(n) time O(1) space.
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
