"""
Traverse the array from right to left, tracking the maximum seen so far.
For each index, assign the current rightMax (the greatest element to its right) before updating rightMax with the current element.
The last index always gets -1 since there's nothing to its right.
O(n) time for a single pass, O(1) extra space besides the output array.
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans