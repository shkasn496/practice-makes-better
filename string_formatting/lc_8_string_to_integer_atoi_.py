# https://leetcode.com/problems/string-to-integer-atoi/description/
"""
Solution 1: Handle different corner cases
Runtime 28 ms Beats 96.41%
Memory 13.8 MB Beats 69.62%
TC: O(N)
SC: O(1)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1#default positive sign
        num = 0
        isDigit=0 #handle edge case for num
        signUpdate = 0 #handle edge case "+-12"
        for c in s:
            if c == ' ':
                if isDigit>0:return num*sign
                elif signUpdate>0 and not num:return 0
                continue
            elif c in {'-','+'}:
                if isDigit>0:return num*sign
                sign=1 if c=='+' else -1
                signUpdate+=1
            elif signUpdate > 1:return 0
            elif c.isdigit():
                num = num*10+int(c)
                isDigit+=1
            elif not c.isdigit():break
        if -2**31<=num*sign <=2**(31)-1:return num*sign
        elif sign<0:return -2**31
        return 2**(31)-1