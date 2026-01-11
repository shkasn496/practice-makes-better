# https://leetcode.com/problems/n-th-tribonacci-number/description
"""
Solution 1: DP with Tabulation
TC: O(n)
SC : O(1)
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        first, second, third = 0, 1, 1
        for i in range(3, n+1):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
        return third
    