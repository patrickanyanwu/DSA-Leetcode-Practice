"""
  We set 2 pointers, 1 at the start and one at the end of the array
  we also keep track of 2 variables which keeps track of the known max to the left and the known max to the right of the array
  now as we loop through we check if the max to the left is less than the right, then we get the amount of water we can store at that index
  by getting the miniumum boundary between the left and right and minus that value by the number at height[i]
  if that value is greater than 0 it is a valid water trapping index so we increase our count by that much.
  This works as if maxleft is less than maxright even though the maxright might not actually be the max at the right
  we know in our algorithm we are getting the minimum between the 2 so it doesnt matterif we dont have the actual maxright
  Vice cersa for if the maxright is greater than or equal.
  O(n) time O(1) space
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = 0
        maxright = 0
        count = 0
        l, r = 0, len(height) - 1

        while l <= r:
            if maxleft < maxright:
                curr = min(maxleft, maxright) - height[l]
                if curr > 0:
                    count += curr
                maxleft = max(maxleft, height[l])
                maxright = max(maxright, height[r])
                l += 1
            else:
                curr = min(maxleft, maxright) - height[r]
                if curr > 0:
                    count += curr
                maxleft = max(maxleft, height[l])
                maxright = max(maxright, height[r])
                r -= 1
        return count
