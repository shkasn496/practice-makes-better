# https://leetcode.com/problems/add-binary/description/

"""
Solution 1: simple reversed list and perform binary addition per digit

Runtime 33 ms Beats 97.52%
Memory 16.3 MB Beats 45.40%

TC:O(max(a, b))
SC:O(1) not considering result
""" 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):return self.addBinary(b, a)
        i=0
        a, b = list(reversed(a)), list(reversed(b))
        carry = 0
        result = []
        while i<len(a):
            a_ = int(a[i])
            b_ = int(b[i]) if i<len(b) else 0
            val = carry
            carry = 0
            if val + a_ > 1:
                carry = 1
                val = 0
            else: val += a_
            if val + b_ > 1:
                carry = 1
                val = 0
            else: val += b_
            result.append(str(val))
            i+=1
        if carry:result.append(str(carry))
        return "".join(list(reversed(result)))