# https://leetcode.com/problems/powx-n/description/
"""
Solution : Equation 
        #  x^n = {# if n is odd
        #                 x * (x^2)^((n-1)/2)
        #         # if n is even
        #                 (x^2)^((n)/2)

Runtime 37 ms Beats 54.13%
Memory 16.3 MB Beats 11.47%
TC:O(logN)
SC:O(1) +logN for recursive stack
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #  x^n = {# if n is odd
        #                 x * (x^2)^((n-1)/2)
        #         # if n is even
        #                 (x^2)^((n)/2)
        def func(base, exponent):
            if exponent==0:return 1
            elif exponent % 2==0: # even power
                return func(base*base, exponent // 2)
            return base * func(base * base, (exponent - 1) // 2) # odd power
        f = func(x, abs(n))
        return f if n>=0 else 1/f