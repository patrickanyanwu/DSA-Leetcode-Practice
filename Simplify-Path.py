"""
  First we split the path by "/".
  then we loop through each part and if the part is "" meaning it was an extra slash we ignore
  or if the part is a singular dot we ignore it also,
  if the part is 2 dots we pop from the stack as its going to the parent directory,
  else we jusy append the part to the stack,
  we then return a / followed by joining the stack with / inbeteen.
  O(n) time O(n) space
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
