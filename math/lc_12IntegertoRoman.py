# https://leetcode.com/problems/integer-to-roman/description/
"""
Solution 1: Subtract number from roman numeral no in descending order

Runtime 44 ms Beats 96.54%
Memory 14 MB Beats 35.43%

TC=SC=O(1)
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [ ('M',1000), ('CM',900),('D',500),('CD',400),
                    ('C',100),('XC',90),('L',50),('XL',40),('X',10),
                    ('IX',9),('V',5),('IV',4),('I',1)]
        substring=""
        for symbol, no in mapping:
            if no==0:break
            if no > num:continue
            if no==num:return substring+symbol
            while no <=num:
                num-=no
                substring+=symbol
        return substring

"""
Solution 2: Divide number with roman value to get frequency of occurrences and make new number as remainder

Runtime 54 ms Beats 84.42%
Memory 14 MB Beats 35.43%

TC=SC=O(1)
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [ ('M',1000), ('CM',900),('D',500),('CD',400),
                    ('C',100),('XC',90),('L',50),('XL',40),('X',10),
                    ('IX',9),('V',5),('IV',4),('I',1)]
        substring=""
        for symbol, no in mapping:
            if no==0:break
            if no > num:continue
            if no==num:return substring+symbol
            freq = num//no
            num%=no
            substring+=symbol*freq
        return substring