""""We split the words string to get a list of all the words in s, if the length of the split is not equal to the length of our pattern we return False,
we then make 2 hashmaps, one for characters to words and one for words to characters this is to help with edge cases.
while we loop through each character and word we check if they are in the maps and dont map to each other in both maps we return false.
Otherwise we map them both in our maps, if the loop finishes then it is a valid pattern.
O(n) tine O(1) space.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        chartoword = {}
        wordtochar = {}
        for char, word in zip(pattern, words):
            if (char in chartoword and chartoword[char] != word) or (word in wordtochar and wordtochar[word] != char):
                return False
            chartoword[char] = word
            wordtochar[word] = char
        return True
