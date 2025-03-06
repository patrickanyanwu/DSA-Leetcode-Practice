"""We look at the maximum number and the minimum number as we can only have a common prefix that has at most the amount of characters in the minimum word.
We check it with the maximum word as if it is shared with the max (max is calculated by alphabetical order) we increment r.
We then return with xtring slicing the maximum word to ensure we dont go out of range.
O(n) time O(1) space"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxi = max(strs)
        mini = min(strs)
        r = 0
        while r < len(mini):
            if maxi[r] == mini[r]:
                r += 1
            else:
                break
        return maxi[:r]
