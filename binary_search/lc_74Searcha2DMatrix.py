# https://leetcode.com/problems/search-a-2d-matrix/description/
"""
Solution: BInary Search

Runtime 34 ms Beats 99.61%
Memory 14.4 MB Beats 41.14%

TC: O(log(m*n))
SC: O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix[0][0]<= target <=matrix[-1][-1]:return False
        m,n = len(matrix), len(matrix[0])
        left, right = 0, (m*n)-1
        while left <= right:
            mid_idx = left+(right-left)//2
            (r,c)=mid_idx//n, mid_idx%n
            if matrix[r][c]==target:return True
            elif matrix[r][c]<target:left=mid_idx+1
            else:right=mid_idx-1
        return False