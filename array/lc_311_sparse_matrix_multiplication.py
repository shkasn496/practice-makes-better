# https://leetcode.com/problems/sparse-matrix-multiplication/description/
"""
Solution 1:
Runtime 198 ms Beats 16.73%
Memory 14 MB Beats 98.61%
TC: O(m*n*k)
SC:O(m*n)
"""
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat2), len(mat2[0])
        mat3 = [[0]*n for r in range(m)]
        for r in range(m):
            for c in range(n):
                if mat1[r]:
                    for i in range(k):
                        mat3[r][c]+=mat1[r][i]*mat2[i][c]
        return mat3

"""
Solution 2: Use hashmap to store non-zero elems
Runtime 114 ms Beats  49.7%
Memory 14.1 MB Beats 81.41%
TC: O(m*n*k)
SC:O(m*n)+O(nonzero1, nonzero2)
"""
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat2), len(mat2[0])
        mat3 = [[0]*n for r in range(m)]
        mat1_n = {(r,c):mat1[r][c] for r in range(m) for c in range(k) if mat1[r][c]!=0}
        mat2_n = {(r,c):mat2[r][c] for r in range(k) for c in range(n) if mat2[r][c]!=0}
        for r in range(m):
            for c in range(n):
                for i in range(k):
                    if (r,i) in mat1_n and (i,c) in mat2_n:
                        mat3[r][c]+=mat1[r][i]*mat2[i][c]
        del mat1_n, mat2_n
        return mat3