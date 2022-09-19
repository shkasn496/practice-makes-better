"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Success
Details 
Runtime: 168 ms, faster than 99.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.7 MB, less than 80.89% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
TC: O(nlogn)+O(n^2) ~ O(n^2)
SC: O(n^2)
"""
class Solution: #brute force solution
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return list(sorted(col for row in matrix for col in row))[k-1]
