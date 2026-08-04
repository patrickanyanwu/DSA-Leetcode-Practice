"""
  Generate a list of all mappings of symbols to numbers,
  then loop through the list from largest to smallest
  if the number divides into the current number in the sym_list
  we add that symbol to our result the amount of times the number divides into it
  we then % the num by the number in order to look at the rest of the num.
  O(n) time O(n) space.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        sym_list = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100],
         ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]   
        
        res = ""

        for sym, number in sym_list:
            if num // number:
                res += sym * (num // number)
                num %= number
        return res
