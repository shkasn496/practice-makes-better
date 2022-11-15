# https://leetcode.com/problems/license-key-formatting/description/
"""
Solution:

TC: O(n)
SC: O(1)(result isn't considered here)
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if len(s)==1 and k==1: return s.upper()
        group=0
        result=""
        for c in reversed(s):
            if c =="-":continue
            if group==k:
                result="-"+result
                group=0
            if c.isalpha:
                result=c.upper()+result
            else: result=c+result
            group+=1
        return result