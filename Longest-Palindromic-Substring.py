"""
  For each index in our word we start with 2 pointers. The algorithm starts from the index and expands outwards to check for palindromes.
  for the case of odd (in length) palindromes we start the 2 pointers on the same character,
  for the case of even (in length) palindromes we start r one after l.
  we keep track of indeces using the res array and we keep track of lengths using a variable.
  We then return the string slicing of the longest palindromic substring.
  O(n ^ 2) time O(1) space.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res = [0, 0]
        reslen = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    res = [l, r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    res = [l, r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
        return s[res[0]: res[1]]
