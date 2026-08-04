"""
  We run dfs from each on each height on the top and left of the grid and we mark every node that could go to the pacific,
  next we run dfs on every node on the bottom and right and mark every node that can go to the atlantic,
  if any node has already been proved to be able to reach the pacific we return to avoid duplicate work.
  We then look through the grid after and every element that is in both our pacific and atlantic set we add it to our result.
  O(m * n) time and O(m * n) space.
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
