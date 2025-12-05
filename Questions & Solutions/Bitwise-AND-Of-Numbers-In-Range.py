class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        I found the common prefix of left and right in their binary
        representations. The key insight is that ANDing all numbers in a range
        preserves only the bits that remain constant throughout the range. I
        repeatedly right-shift both numbers until they become equal, tracking
        the shift count. Once they're equal, I've found the common prefix. I
        then left-shift back by the same amount to restore the position. The
        bits that changed during the range become 0 in the result, while the
        common prefix bits are preserved.
        O(log n) time O(1) space
        """
        shift = 0
        
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        return left << shift