# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/description/
"""
Solution 1: Optimal Binary search solution
Runtime 92 ms Beats 100%
Memory 14.3 MB Beats 39.52%
TC: O(m*log(n))
SC:O(1)
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        col, found=n-1, False
        for r in range(m):
            #only need to binary check if there is element 
            # less than the minimum column element
            if not binaryMatrix.get(r,col):continue
            found=True
            left, right = 0, n-1
            while left < right:
                mid=left+(right-left)//2
                elem = binaryMatrix.get(r,mid)
                if not elem:left=mid+1
                else:
                    right=mid
                    col=min(col,mid)
        return col if (col <= n-1) and found else -1
    