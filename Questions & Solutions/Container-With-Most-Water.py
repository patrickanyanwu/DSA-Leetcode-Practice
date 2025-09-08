"""Start the left pointer at the beginning of the array of height and the right pointer at the end.
While l < r we calculate the max area by using (r – l) being the distance along the x-axis and we use the height of the smallest height between l and r and multiply the distance by height to get the area,
we then keep track of max with the maximum variable.
We only increment the index of the smaller height between the 2 in order to find a potentially bigger height.
O(n) time O(1) space"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0
        while l < r:
            if heights[l] < heights[r]:
                amount = (r - l) * heights[l]
                l += 1
            else:
                amount = (r - l) * heights[r]
                r -= 1
            maximum = max(amount, maximum)
        return maximum
