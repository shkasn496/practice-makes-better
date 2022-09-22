"""
Success
Details 
Runtime: 41 ms, faster than 97.99% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 88.87% of Python3 online submissions for Search a 2D Matrix.
TC: O(M*log(N)) where M=rows, N=columns
SC:O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        def binarySearch(row):
            left, right = 0, N-1
            while(left<right):
                mid=left+(right-left)//2
                if matrix[row][mid]==target:return True
                elif matrix[row][mid]>target:right=mid
                else:left=mid+1
            return matrix[row][left]==target
        for r in range(M):
            if matrix[r][0]<=target<=matrix[r][N-1]:return binarySearch(r)
        return False