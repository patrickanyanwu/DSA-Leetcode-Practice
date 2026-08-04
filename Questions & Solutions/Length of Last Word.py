"""Two while loops with pointers, while we have spaces at the end we keep decrementing r untill we have reached our first actual character,
after that we set l to that and begin our while loop while we have a valid character we decrement l.
Once we hit a Space again or we hit the end of the array we stop the loop and the length of the words is r - l
O(n) time O(1) space."""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while s[r] == " " and r > 0:
            r -= 1
        l = r
        while s[l] != " " and l >= 0:
            l -= 1
        return r - l
    
