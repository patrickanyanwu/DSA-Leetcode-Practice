"""
  Append each letter in s into a stack and if we see a star we pop from the stack instead.
  If we see a star and the stack is empty we immediately return the empty string,
  return the stack joined into a string.
  O(n) time O(n) space.
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for letter in s:
            if letter == "*":
                if stack:
                    stack.pop()
                else:
                    return ""
            else:
                stack.append(letter)
        return "".join(stack)
