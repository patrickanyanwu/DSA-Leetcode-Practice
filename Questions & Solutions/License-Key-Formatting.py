
"""
    We start by removing all the - 's from the string and setting it all to uppercase,
    we then initialize a result array which will hold each made group,
    we then enter our loop which inside we will append the last k characters to result
    we then remove the last k characters from s and the loop runs while the length
    of s is greater than k. Afterwards we append the last remaining part of s to result.
    We then return a - seperated version of the reversed result array.
    O(n) time O(n) space
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        result = []
        while len(s) > k:
            result.append(s[-k:])
            s = s[:-k]
        result.append(s)
        
        return "-".join(result[::-1])