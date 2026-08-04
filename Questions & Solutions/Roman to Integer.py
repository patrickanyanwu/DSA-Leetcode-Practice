"""Have a hasmap with key being roman character and value being its numberic value,
while looping through we check if the number ahead is greater than the current number then we add the larger number minus the smaller numberas thats how roman numerals work.
O(N) time O(1) space.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        count = 0
        l = 0
        while l < len(s):
            if l + 1 < len(s) and roman_values[s[l]] < roman_values[s[l + 1]]:
                count += roman_values[s[l + 1]] - roman_values[s[l]]
                l += 2 
            else:
                count += roman_values[s[l]]
                l += 1  

        return count
