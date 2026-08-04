"""Stored opening brackets in a set to ensure O(1) checks. Made hashmap with key being the closing brackets and values is its corresponding opening brackets.
We initialize a stack to hold each opening bracket in the input string.
For every bracket in the input string if its an opening bracket we push it into our stack,
If it’s a closing bracket we check if the stack is empty first and if it is we return false as there is too many closing brackets in the string,
if the stack is not empty we pop the last item in the stack and check its equal to the current closing brackets corresponding opening bracket, if its not equal at any point we return false,
if not we continue.
The last check checks if the stack is empty (there were valid parentheses). 
O(n) time O(n) space."""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        hasht = {")": "(", "}": "{", "]": "["}
        set1 = set(["(", "{", "["])
        stack = []
        for brack in s:
            if brack in set1:
                stack.append(brack)
                continue
            if len(stack) != 0:
                if brack in hasht and stack.pop() != hasht[brack]:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
