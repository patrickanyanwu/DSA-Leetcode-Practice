"""
  We have 4 pointers, 1 for the bottom, top, left and right. Now for each layer of the matrix we swap the cells accordingly.
  This is done by setting a temp variable at the topleft cell and then we set the topleft equal to the bottom left,
  the bottom left ewual to the bottom right and the top right ewual to the top left.
  Our for loop takes care of doing the same with each cell in the layer we are in.
  O(n^2) time O(1) space.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                temp = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l] 
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = temp
            l += 1
            r -= 1
