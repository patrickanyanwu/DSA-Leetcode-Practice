"""
  For each index in our word we start with 2 pointers. The algorithm starts from the index and expands outwards to check for palindromes.
  A countmis initialized at the beginging which we will increment accordingly.
  for the case of odd (in length) palindromes we start the 2 pointers on the same character,
  for the case of even (in length) palindromes we start r one after l.
  We then return the count.
  O(n ^ 2) time O(1) space.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
