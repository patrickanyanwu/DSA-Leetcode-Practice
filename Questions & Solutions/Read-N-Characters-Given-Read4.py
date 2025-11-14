"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

I repeatedly called read4 to read chunks of
up to 4 characters into a buffer. I copied
characters from the buffer to the output,
stopping when I reached n characters or the
file ended.
O(n) time O(1) space
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total = 0
        buf4 = [''] * 4

        while total < n:
            count = read4(buf4) 
            if count == 0:
                break

            for i in range(min(count, n - total)):
                buf[total] = buf4[i]
                total += 1

        return total