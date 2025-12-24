"""
I used a stack to track valid scores and maintain a running total. For each
operation, I handle four cases: 'C' removes the last score from both stack
and total, 'D' doubles the last score and adds it, '+' sums the last two
scores and adds the result, and numeric strings are converted to integers
and added. I maintain a total_sum variable throughout to avoid recalculating
the sum at the end. The stack keeps track of all valid scores needed for
operations like 'D' and '+'. This efficiently processes all operations in one
pass while maintaining the necessary history.
O(n) time O(n) space
"""


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_sum = 0
        for op in operations:
            if op == "C":
                total_sum -= stack.pop()
            elif op == "D":
                new_val = stack[-1] * 2
                stack.append(new_val)
                total_sum += (new_val)
            elif op == "+":
                new_val = stack[-1] + stack[-2]
                stack.append(new_val)
                total_sum += (new_val)
            else:
                stack.append(int(op))
                total_sum += int(op)
        return total_sum