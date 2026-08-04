"""
  Have a pointer idx which stays at the index in the array where we can make our next inplace reassignment.
  We now have a sliding window where r increases while we the characters at l and r are equal.
  Once they are not equal or we hit the last character we set the character at idx to the character at l,
  we then get the length of the window and turn it into a stting so we can put it in the array,
  for each character in the length we set the character at idx to that letter and increment idx if the length is more than 1.
  O(n) time O(1) sapce.
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        idx = 0

        for r in range(len(chars)):
            if chars[r] != chars[l]:
                chars[idx] = chars[l]
                idx += 1
                length = r - l
                if length > 1:
                    string = str(length)
                    for c in string:
                        chars[idx] = c
                        idx += 1
                l = r
            if r == len(chars) - 1:
                chars[idx] = chars[l]
                idx += 1
                length = r - l + 1
                if length > 1:
                    string = str(length)
                    for c in string:
                        chars[idx] = c
                        idx += 1
        return idx
