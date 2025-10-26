class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xxor = 0
        for i in range(n):
            xxor ^= (start + 2 * i)
        return xxor