"""Initialized a hashmap with the keys being the frequency of letters and the values being the list of words in the input array that have the same frequency of letters. 
The keys of a dictionary can't be lists so a tuple is used to hold the frequency. Returned list of values of hashmap. O(n^2) time O(n) space"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            res[tuple(count)].append(word)
        return res.values()
