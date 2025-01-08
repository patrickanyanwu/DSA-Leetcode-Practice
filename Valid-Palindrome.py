"""For every character in the input string we make a new string with each character that is a letter or number. We then reverse that string and check if its equal to the normal string.
O(n) time O(n) space."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        prev_string = ""
        for letter in s.lower():
            if (letter >= "a" and letter <= "z") or (letter >= "0" and letter<= "9"):
                prev_string += letter
        rev_string = "".join(prev_string[::-1])
        if prev_string == rev_string:
            return True
        return False
