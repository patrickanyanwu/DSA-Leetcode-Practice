"""Have two pointers, one at the first string and one at the second. We then begin a for loop and if the current letter we are on corresponds to the current letter in the subsequence we are on,
er increment the subsequence count. If at any point the count is equal to the length of the subsequence we return True.
O(n) time O(1) space."""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if not s:
            return True
        if not t:
            return False
        count = 0
        for r in range(len(t)):
            if t[r] == s[count]:
                count += 1 
            if count == len(s):
                return True
        return False
