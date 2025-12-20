"""
    I used hash maps to find the extra character added to string t. I
    create character frequency counters for both strings s and t. Then I
    iterate through t's counter and check if each character either doesn't
    exist in s or has a different frequency. The first character that
    doesn't match is the added one. I handle the edge case where s is empty
    by returning t directly. This approach efficiently identifies the extra
    character by comparing frequencies.
    O(n) time O(n) space
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        c1, c2 = Counter(s), Counter(t)

        for key, value in c2.items():
            if key not in s:
                return key
            if c1[key] != value:
                return key