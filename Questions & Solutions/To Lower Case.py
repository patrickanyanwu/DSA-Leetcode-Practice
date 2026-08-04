"""
I converted the string to lowercase by iterating through each character
and applying the lower() method. I use a list comprehension to process
each character, converting uppercase letters to lowercase while leaving
other characters unchanged. Then I join all the characters back into a
single string. This approach is straightforward and leverages Python's
built-in string methods. The lower() method handles the ASCII conversion
automatically for all uppercase letters.
O(n) time O(n) space
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([char.lower() for char in s])