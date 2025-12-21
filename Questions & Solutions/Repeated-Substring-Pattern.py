"""
    I checked if the string can be formed by repeating a substring by
    trying all possible substring lengths. I iterate from length 1 to n//2
    since any repeating pattern must be at most half the string length. For
    each length, I skip if n isn't divisible by it, as the pattern must
    repeat evenly. I then check if repeating the first 'length' characters
    exactly n//length times recreates the original string. If I find a
    match, I return True. If no valid pattern exists after checking all
    lengths, I return False.
    O(n²) time O(n) space
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length != 0:
                continue
            if s[:length] * (n // length) == s:
                return True
        return False