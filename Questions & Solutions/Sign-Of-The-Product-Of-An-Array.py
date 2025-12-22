"""
    I determined the sign of the product by counting negative numbers
    rather than computing the actual product. I iterate through the array
    and immediately return 0 if I encounter a zero, since any product with
    zero is zero. For non-zero numbers, I count how many are negative. The
    product is positive if there's an even number of negatives (including
    zero negatives), and negative if there's an odd number. This avoids
    overflow issues from multiplying large numbers and is more efficient
    than computing the actual product.
    O(n) time O(1) space
"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0

        for num in nums:
            if num == 0:
                return num
            neg_count += (num < 0)

        return 1 if not neg_count % 2 else -1



