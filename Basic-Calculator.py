"""
  We keep track of the current number were on. the sign we have to multiply by, our stack and our result number,
  now we loop through the string and if we find a digit we construct the number accordingly
  if we hit a + sign we add our number * sign to our result and the same for - but if we hit a minus we change our sign to be -
  this ensure the next number we see its negative gets added to our result
  now when we hit an opening bracket we append our current result and sign to our stack then set our result to be 0 and sign to by positive
  so we can evaluate inside the brackets, when we hit a closing bracket we pop our previous result and sign from the stack and we multiply the result by the sign
  and add the previous result to our new result, num is reset after every calculation.
  At the end we add the final number to our result.
  O(n) time O(n) space
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0 
        num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        res += sign * num
        return res
