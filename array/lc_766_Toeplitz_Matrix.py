# https://leetcode.com/problems/toeplitz-matrix/description/
"""
Solution 1: Iterate over all rows and cols and break 
            if row and col elem not equal to previous elem

Runtime 90 ms Beats 62.13%
Memory 16.3 MB Beats 17.30%
TC:O(m*n)
SC:O(1)
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for r in range(1, m):
            for c in range(1,n):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True

"""
Solution 2: Solution leveraging diagonal property
Runtime 90 ms Beats 62.13% 
Memory 16.4 MB Beats 17.30%
TC:O(m*n)
SC:O(m+n)
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        diag={}
        for r in range(m):
            for c in range(n):
                if (r-c) not in diag:
                    diag[(r-c)]=matrix[r][c]
                elif matrix[r][c] != diag[(r-c)]:
                    del diag
                    return False
        del diag
        return True
