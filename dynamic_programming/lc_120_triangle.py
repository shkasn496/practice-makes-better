# https://leetcode.com/problems/triangle/description/

"""
Solution 1: Bottom Up DP solution with memory saving

Runtime 0ms Beats 100.00%
Memory 18.43 MB Beats 99.76%

TC: O(N*M) where N is len(triangle)
SC: O(M) where M is len(triangle[-1])    
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[-1][-1]
        N = len(triangle)
        cache = triangle[N-1]
        for i in range(N-2, -1, -1):
            for j in range(len(triangle[i])):
                cache[j] = min(cache[j]+triangle[i][j], cache[j+1]+triangle[i][j])
        return cache[0]