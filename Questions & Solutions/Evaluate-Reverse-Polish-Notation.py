"""
  We add each number in the expression to a stack,
  when we reach a sign we pop the last 2 elements from the stack and perform the calculation
  then push it back into the stack to be used in further calculations.
  At the end we return the final element in the stack (the full evaluation)
  O(n) time O(n) space
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
