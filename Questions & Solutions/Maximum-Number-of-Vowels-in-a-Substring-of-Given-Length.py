"""
  Used a vowel set to allow for O(1) checks for if a letter is a vowel.
  We then extend our window to the fixed length of k and count the number of vowels in the window.
  We then slide our window along the string and keep track of the vowel count accordingly with our l and r pointers.
  O(n) time O(1) space.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        maxCount = 0
        count = 0
        for r in range(k):
            if s[r] in vowels:
                count += 1
        maxCount = max(maxCount, count)
        l = 0
        r = k

        while r < len(s):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            l += 1
            r += 1
            maxCount = max(count, maxCount)
        return maxCount
