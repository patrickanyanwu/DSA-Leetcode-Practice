"""
I created a signature for each word using
a frequency array of 26 letters. I compared
each word's signature with the previous one,
only keeping words with different signatures
to remove consecutive anagrams.
O(n * m) time O(n) space
"""

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def signature(word: str):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            return tuple(freq)

        res = [words[0]]
        prev_sig = signature(words[0])

        for i in range(1, len(words)):
            sig = signature(words[i])
            if sig != prev_sig:
                res.append(words[i])
                prev_sig = sig
        return res