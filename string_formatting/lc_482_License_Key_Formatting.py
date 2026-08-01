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

"""
Solution 2: Use list to hold result as lists are mutable while strings are immutable

"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        if n < 2:
            return s.upper() if s != "-" else ""
        result = []
        for c in reversed(s):
            if c == "-":continue
            c = c.upper()
            if not result:
                result.append([c])
                continue
            if len(result[-1]) < k:
                result[-1] = [c] + result[-1]
            else:
                result.append([c])
        result = "-".join("".join(lst) for lst in reversed(result))
        return result