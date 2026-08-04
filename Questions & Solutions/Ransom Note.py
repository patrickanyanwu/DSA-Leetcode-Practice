"""Use a hashmap with keys being the letter in the string and the value being the frequency of the letter in the string,
Now for every key in the ransomnote dictionary we check if the key is in our magazine, if not then the magazine does not have the letter and it cant be constructed.
so return False. Also if the frequency in our ransomnote is greater than what we can use to construct it we return False.
If loop finished we have sufficient letters so we return True.
O(nO time O(n) space.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countr = Counter(ransomNote)
        countm = Counter(magazine)
        for key, value in countr.items():
            if key in countm:
                if value <= countm[key]:
                    continue
                else:
                    return False
            return False
        return True
