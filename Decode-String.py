"""
  We loop through each character in s and if the cahracter is not a digit we add it to our result,
  if it is a digit we get the full number with a while loop then we use a stack to find where the opening bracket closes,
  then we recursively call the function on the characters enclosed by the brackets then multiply the result by the number.
  O(n) time O(n) space.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        r = 0
        res = ""
        while r < len(s):
            if s[r].isdigit():
                num = ""
                while s[r].isdigit():
                    num += s[r]
                    r += 1
                num = int(num)
                l = r + 1
                stack = []
                stack.append(s[r])
                r += 1
                while stack:
                    if s[r] == "[":
                        stack.append("[")
                    elif s[r] == "]":
                        stack.pop()
                    r += 1
                res += (self.decodeString(s[l:r - 1]) * num)
            else:
                res += s[r]
                r += 1
        return res
