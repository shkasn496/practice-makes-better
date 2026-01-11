# https://leetcode.com/problems/fibonacci-number
"""
Solution 1: DP with tabulation

TC: O(N)
SC: O(1)
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        first, second = 0, 1
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return second    