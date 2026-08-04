"""Start left pointer at the beginning of the array and right pointer 1 after the beginning. We then check if the number at the right pointer is higher than the one on the left pointer,
if so we calculate its difference and keep track of the max. 
If the number on the right is less than the left we move our left pointer to the right pointer after all checks the size of our window increases ( r += 1). 
O(n) time O(1) space"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                diff = prices[r] - prices[l]
                max_prof = max(max_prof, diff) 
            r += 1
        return max_prof
                
