"""We use a fixed length sliding window and search the string for the needle, if the current substring is not the needle we increment our left pointer and check a new window.
If found we return index l as that is the beginning of the occurence in the haystack.
O(n) time O(1) space""""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_need = len(needle)
        l = 0
        for r in range(len_need, len(haystack) + 1):
            if haystack[l:r] == needle:
                return l
            else:
                l += 1
        return -1
