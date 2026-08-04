"""
  Use hashmaps for each row column and square with the key being the row,
  col or square and the value being a set containing all number in them specific places.
  Now as we loop through the grid we add each number to its row and columns hashmap
  and for the squares we integer divide their indices to tell us what square we are in
  we then store a tuple of the square as the key for the hashmap and add the current number.
  if a duplicate is ever found we return false and if the loop finishes we return true.
  O(9 ^ 2) time O(9 ^ 2) space
  
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                cell = board[r][c]
                if (cell in rows[r] or cell in cols[c] or cell in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                squares[(r // 3, c // 3)].add(cell)
        return True
