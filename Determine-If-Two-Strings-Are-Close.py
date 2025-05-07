"""
  First check if their lengths are not equal we return false.
  Now we get the frequency count for each word,
  If the set of word1 is not equal to the set of word 2 (they dont have the same distinct characters) we return false.
  If they are equal we check if we have equal frequency counts (we can replace letters to get the other).
  O(n) time O(1) space as max size of anything is 26.
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if set(word1) != set(word2):
            return False
        return sorted(counter1.values()) == sorted(counter2.values()) 
