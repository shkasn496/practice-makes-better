# https://leetcode.com/problems/roman-to-integer/description/
"""
Solution:

Runtime 38 ms Beats 99.4%
Memory 14 MB Beats 30.32%

TC=SC=O(1)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1,"V":5,"X":10, "L":50, "C":100, "D": 500, "M":1000}
        integer= i = 0
        while i < len(s):
            val1 = mapping[s[i]]
            if i==len(s)-1:return integer + val1
            val2 = mapping[s[i+1]]
            if val1< val2: 
                integer+=val2-val1
                i+=2
            else: 
                integer+=val1
                i+=1
        del mapping
        return integer