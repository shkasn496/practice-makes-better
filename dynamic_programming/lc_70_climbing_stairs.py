# https://leetcode.com/problems/climbing-stairs/description
"""
Solution 1: DP with tabulation

TC: O(n)
SC: O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1 : return 1
        first, second = 1, 1
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return second
    
