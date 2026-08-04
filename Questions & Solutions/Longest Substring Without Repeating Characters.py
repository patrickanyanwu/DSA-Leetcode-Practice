""" We start left and right pointer at the beginning of the string, we initialize a set to hold characters within the window (the substring). 
If the character at index r is not in the set we add it to the set and increment r by 1, if the character at r is in the set (a duplicate) we remove the character at l from the set and increment l by 1 to find a new substring.
We then calculate the length as r – l + 1 and keep track of max. 
O(n) time O(m) space, m being longest substring."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        set1 = set()
        while r < len(s):
            if s[r] not in set1:
                set1.add(s[r])
                diff = (r - l) + 1
                r += 1
            else:
                set1.remove(s[l])
                l += 1
            longest = max(longest, diff)
        return longest
