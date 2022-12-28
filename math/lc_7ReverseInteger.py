# https://leetcode.com/problems/reverse-integer/description/
"""
Solution 1: reverse string

Runtime 22 ms Beats 99.81%
Memory 13.7 MB Beats 99.93%

TC: O(n)
SC:O(n)
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>=0 else -1
        num = str(abs(x))
        num = sign * int(num[::-1])
        if -(2**31)<=num<= (2**31)-1:
            return num
        return 0