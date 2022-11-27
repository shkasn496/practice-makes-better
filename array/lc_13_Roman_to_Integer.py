# https://leetcode.com/problems/roman-to-integer/description/
"""
Runtime 44 ms Beats 96.98%
Memory 13.9 MB Beats 77.8%

TC : O(n)
SC : O(1)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1,"V":5,"X":10, "L":50, "C":100, "D": 500, "M":1000}
        integer = 0
        i=0
        while i < len(s):
            val1 = mapping[s[i]]
            if i==len(s)-1:
                integer+=val1
                break
            val2 = mapping[s[i+1]]
            if val1< val2: 
                integer+=val2-val1
                i+=2
            else: 
                integer+=val1
                i+=1
        return integer