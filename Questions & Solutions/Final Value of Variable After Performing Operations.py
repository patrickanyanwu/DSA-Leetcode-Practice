"""O(n) time"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if operation[0] == "-" or operation[-1] == "-":
                X -= 1
            else:
                X += 1
        return X