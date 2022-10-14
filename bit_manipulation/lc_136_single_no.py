# https://leetcode.com/problems/single-number/
"""
Success
Details 
Runtime: 142 ms, faster than 91.49% of Python3 online submissions for Single Number.
Memory Usage: 16.8 MB, less than 49.35% of Python3 online submissions for Single Number.
TC: O(n)
SC:O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        # xor on twice appeared elems will make result 0
        # XOR operator in python removes duplicates
        # example: [5,4,3,4,3] => will be (((5 xor 4) xor 3) xor 4) xor 3) xor 4)))) output will be 5
        # since xor is also commutative you can arrange it whenever you want: 
        # (4 xor 4) xor (3 xor 3) xor 5 => will result in 0 xor 0 xor 5 => thus only 5 is the unique number
        for elem in nums: result^=elem
        return result