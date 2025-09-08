"""
  Firstly we store a count of the frequency of every row in a hashmap,
  next we loop through each column and check if that column is in the hashmap (we have a valid pair),
  if it is we increment our count of pairs by the frequency of the row in the hashmap (the number of pairs we can make with that column).
  O(n ^ 2) time O(n ^ 2) space.
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = {}
        for row in grid:
            row = tuple(row)
            counter[row] = counter.get(row, 0) + 1
        count = 0
        for r in range(len(grid)):
            col = (grid[0][r],)
            for j in range(1, len(grid)):
                col += (grid[j][r],)
            count += counter.get(col, 0)
        return count
