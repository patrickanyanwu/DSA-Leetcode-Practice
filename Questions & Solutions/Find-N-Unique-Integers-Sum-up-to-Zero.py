"""
I used two pointers to create pairs of negative and positive numbers that cancel out.
Starting with an array of zeros, I placed negative values on the left and positive values on the right,
ensuring they sum to zero. If n is odd, the middle element remains 0.
O(n) time and space.
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        l, r = 0, n - 1
        while l < r:
            res[l] -= (1 + l)
            res[r] += (1 + l)
            l += 1
            r -= 1
        return res
    
