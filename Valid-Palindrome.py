"""For every character in the input string we set left and right pointers, if either of them are a space or not alphanumereic we move the appropriate pointer.
If they are both alphanumeric we check if they are equal, if they are we move both pointers and if not we return False as it is not a palindrome.
O(n) time O(1) space."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        if len(s) == 1:
            return True
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == " ":
                l += 1
                continue
            if s[r] == " ":
                r -= 1
                continue
            letter1 = s[l].lower()
            letter2 = s[r].lower()
            if letter1.isalnum() and letter2.isalnum():
                if letter1 == letter2:
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                if not letter1.isalnum():
                    l += 1
                if not letter2.isalnum():
                    r -= 1
        return Tr
