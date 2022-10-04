"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Success
Details 
Runtime: 168 ms, faster than 99.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.7 MB, less than 80.89% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
TC: O(n^2logn^2)+O(n^2) ~ O(n^2)
SC: O(n^2)
"""
class Solution: #brute force solution
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return list(sorted(col for row in matrix for col in row))[k-1]
"""
Better Solution : Binary Search + Optimized Counting
Success
Details 
Runtime: 162 ms, faster than 99.77% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.6 MB, less than 79.48% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
TC: O(n* log(max))
SC: O(1)
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count(target):
            count, row, col=0, 0,len(matrix[0])-1
            while row<len(matrix) and col>=0:
                if matrix[row][col]<=target: 
                    count+=col+1
                    row+=1
                else: col-=1
            return count
        left,right = matrix[0][0], matrix[-1][-1]
        while left<=right:
            mid = left + (right-left)//2
            curr_count=count(mid)
            if curr_count >=k: right=mid-1 # we want to check if a smaller no can satisfy this condition as well
            else:left=mid+1
        return left
