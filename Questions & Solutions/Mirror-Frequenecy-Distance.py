"""
    Count each character's frequency, then compare every character with its mirror pair.
    Mirror rule: letters map a<->z, b<->y ... and digits map 0<->9, 1<->8 ...
    Use a seen set so each pair is processed only once and doesn't get double-counted.
    For each new pair, add abs(freq(char) - freq(mirrorChar)) to the answer.
    This captures how unbalanced each mirror pair is.
    O(n) time with O(k) space, where k is number of unique characters.
"""

class Solution:
    def getMirrorChar(self, char):
        if char.isalpha():
            offset = ord(char) - ord("a")
            mirrorindex = ord("z") - offset
        else:
            offset = ord(char) - ord("0")
            mirrorindex = ord("9") - offset
        return chr(mirrorindex)
    def mirrorFrequency(self, s: str) -> int:
        counter = Counter(s)
        seen = set()
        res = 0
        for key, value in counter.items():
            mirrorChar = self.getMirrorChar(key)
            if key in seen or mirrorChar in seen:
                continue
            res += abs(counter[key] - counter[mirrorChar])
            seen.add(key)
            seen.add(mirrorChar)
        return res