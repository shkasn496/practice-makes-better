# https://leetcode.com/problems/add-strings/description/
"""
Solution: Use divmod
Runtime 48 ms Beats 43.61%
Memory 16.7 MB Beats 7.17%
TC:O(n) where n=len(num1) and len(num1)>=len(num2)
SC:O(n)
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':return num1 if num2=='0' else num2
        if len(num2)>len(num1):return self.addStrings(num2,num1)
        carry=0
        output=[]
        i, j = len(num1)-1, len(num2)-1
        while i>=0 or j>=0:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            n3=n1+n2+carry
            carry, n3 = divmod(n3,10)
            output.append(str(n3))
            i-=1
            j-=1
        if carry:output.append(str(carry))
        result="".join(list(reversed(output)))
        del output
        return result