"""
I checked if a number is confusing by simulating a 180-degree rotation. I use
a mapping dictionary where 0, 1, and 8 rotate to themselves, while 6 and 9
swap. I convert the number to a string and iterate through it in reverse order
(since rotation flips position). For each digit, I check if it's rotatable; if
not, I return False immediately. If all digits are rotatable, I build the
rotated string and compare it to the original. A number is confusing if it's
valid (all digits rotatable) but different from its rotation. This handles
both validation and comparison in one pass.
O(log n) time O(log n) space
"""

class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        s = str(n)
        rotated = []

        for ch in reversed(s):
            if ch not in rotate:
                return False
            rotated.append(rotate[ch])

        return ''.join(rotated) != s
