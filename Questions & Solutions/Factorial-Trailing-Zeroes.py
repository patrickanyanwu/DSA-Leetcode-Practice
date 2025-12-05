class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        I counted the number of trailing zeros by finding how many times 10
        divides n!. Since 10 = 2 × 5, and there are always more factors of 2
        than 5 in factorials, I only need to count factors of 5. I divide n by
        5 repeatedly to count multiples of 5, 25 (5²), 125 (5³), etc. Each
        division gives the count of numbers contributing that power of 5. I
        accumulate these counts because numbers like 25 contribute two factors
        of 5. This efficiently counts all factors of 5 without computing the
        factorial itself.
        O(log n) time O(1) space
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count