"""Compare the frequency count of every letter in each string. If they are equal return True. O(n) time O(n) space"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
