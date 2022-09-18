"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Success
Details 
Runtime: 168 ms, faster than 99.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.7 MB, less than 80.89% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return list(sorted(col for row in matrix for col in row))[k-1]
