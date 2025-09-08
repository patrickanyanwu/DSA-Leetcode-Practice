"""
  Use the Counter() function from the collections library which returns a hashmap with the key being an element in arr and value being its frequency.
  Counter()'s values will be an array of all of the frequencies.
  I then return true if the length of the set (as sets remove duplicates) of the frequencies array is equal to the length of the frequencies array.
  O(n) time O(n) space.
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter.values())
