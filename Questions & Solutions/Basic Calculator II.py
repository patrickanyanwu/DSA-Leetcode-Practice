"""
Evaluate the expression in a single left-to-right pass by deferring the application of an operator until the next operator (or the end of the string) is reached.
Build up the current number digit by digit as we scan.
When a +/-/* or / is hit (or we're at the last character), apply the *previous* operator to the number just finished: '+' and '-' push the running "prev" term onto total and start a new signed term, while '*' and '/' fold directly into "prev" since they bind tighter than addition — this naturally gives multiplication/division precedence without a stack.
A custom trunc_div is used instead of Python's // because Python floor-divides toward negative infinity, but this problem requires truncation toward zero for negative results.
After the loop, add the last pending term (prev) to total since there's no trailing operator to trigger it.
O(n) time for a single pass over the string, O(1) space (excluding the input).
"""

class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        prev = 0
        num = 0
        op = '+'

        def trunc_div(a: int, b: int) -> int:
            q = abs(a) // abs(b)
            return -q if (a < 0) != (b < 0) else q

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))

            if ch in '+-*/' or i == len(s) - 1:
                if op == '+':
                    total += prev
                    prev = num
                elif op == '-':
                    total += prev
                    prev = -num
                elif op == '*':
                    prev *= num
                else:
                    prev = trunc_div(prev, num)
                op = ch
                num = 0

        return total + prev