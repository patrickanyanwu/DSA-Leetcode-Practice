"""
    I implemented string multiplication by simulating the grade school
    multiplication algorithm. I first handle the zero case, then create a
    result array of length n+m to store intermediate sums. I iterate from
    right to left through both numbers, multiplying each digit pair and
    adding to the appropriate position in the result array. I handle carries
    by storing the remainder at the current position and adding the quotient
    to the previous position. Finally, I convert the array to a string while
    skipping leading zeros. This mimics manual multiplication digit by digit.
    O(n × m) time O(n + m) space
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + res[i + j + 1]

                res[i + j + 1] = sum_ % 10
                res[i + j] += sum_ // 10

        result = []
        for digit in res:
            if not result and digit == 0:
                continue
            result.append(str(digit))

        return ''.join(result)
