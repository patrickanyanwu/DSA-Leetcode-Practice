"""
  Use res to construct result and use cur to keep track of current line to be justified,
  we loop through the words and we keep a numofletters count, once the amount of words we have plus the amount of spaces we need
  is about to be greater than the maxwidth we start the justification process
  we calculate the amount of spaces we need by using maxwidth - numofletters
  we then loop through that number and for each word in cur we distribute the spaces evenly
  modulo is used to distribute spaces accordingly
  len(cur) - 1 or 1 is used for the case of only one word being in cur we just keep adding spaces to the only word.
  we then add the joined cur array to our result and reset our count and cur.
  The last line is then left justified alone.
  O(n * maxwidth) time O(n) space
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        num_of_letters = 0

        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur = []
                num_of_letters = 0
            cur.append(word)
            num_of_letters += len(word)

        res.append(' '.join(cur).ljust(maxWidth))
        return res
