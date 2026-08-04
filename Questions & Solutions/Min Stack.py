"""
  We keep a stack and minstack which are both arrays,
  minstack holds the current minimum values
  whe we push to our stack we check if this value <= our current minimum
  if it is or if the minstack is empty we append the value to the minstack
  when a user wants to pop we check if that popped value is our current mimum
  if it is we pop from the minstack too.
  O(1) time O(n) space
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
