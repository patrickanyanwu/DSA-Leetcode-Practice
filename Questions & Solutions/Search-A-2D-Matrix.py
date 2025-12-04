class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        I treated the 2D matrix as a flattened 1D sorted array and used binary
        search. I calculate total elements as n * m and set left to 0 and right
        to n * m - 1. For each midpoint index, I convert it back to 2D
        coordinates using row = mid // m and col = mid % m to access the matrix
        value. I then perform standard binary search: if the cell value is less
        than target, I search the right half; if greater, I search the left
        half; if equal, I return True. This leverages the sorted property
        efficiently.
        O(log(n * m)) time O(1) space
        """
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        
        while l <= r:
            mid = (l + r) // 2
            row = mid // m
            col = mid % m
            
            cell = matrix[row][col]
            
            if cell < target:
                l = mid + 1
            elif cell > target:
                r = mid - 1
            else:
                return True
        
        return False