# https://leetcode.com/problems/rotate-image/description/
"""
Solution 1 : Swap 4 corners of the image, rows are top, bottom, cols are left and right
TC: O(n^2)
SC:O(1)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1
        while left < right:
            for i in range(right-left):
                top, bottom = left, right
                # temp store topleft (col +ve shift by i)
                topleft = matrix[top][left+i]
                # store bottomleft in topleft. (row -ve shift by i)
                matrix[top][left+i] = matrix[bottom - i][left]
                # store bottomright in bottomleft (col -ve shift by i)
                matrix[bottom - i][left] = matrix[bottom][right-i]
                # store topright in bottomright (row +ve shift by i)
                matrix[bottom][right-i] = matrix[top + i][right]
                # store topleft in topright
                matrix[top + i][right] = topleft
            left += 1
            right -= 1
        return

"""
Solution 2: Transpose, then flip rows
TC: O(n)
SC: O(1)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose on left diagonal
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # flip rows
        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]