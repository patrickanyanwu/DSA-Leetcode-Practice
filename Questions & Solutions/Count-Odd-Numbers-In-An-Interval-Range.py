"""
    I calculated the count of odd numbers using a mathematical formula
    instead of iterating. The range has (high - low) // 2 pairs of
    even-odd numbers. If either low or high is odd, there's one additional
    odd number not counted in the pairs. I use (low % 2 or high % 2) to
    check if at least one endpoint is odd, adding 1 if true. This avoids
    looping through the range and computes the result in constant time. The
    formula efficiently handles both even and odd range boundaries.
    O(1) time O(1) space
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 or high % 2)