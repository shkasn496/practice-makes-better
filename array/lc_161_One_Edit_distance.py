# https://leetcode.com/problems/one-edit-distance/description/

"""
Solution 1: Non optimized code
Runtime 43 ms Beats 9.87%
Memory 16.4 MB Beats 5.10% 
TC:O(n)
SC:O(1)
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m == n == 0:return False
        if m > n:return self.isOneEditDistance(t,s)#keep s less than or equal to t
        if n - m > 1:return False #more than one edit distance
        for i in range(m):
            if s[i]!=t[i]:
                if m==n:return s[i+1:]==t[i+1:]
                return s[i:]==t[i+1:]
        return m+1 == n
    
"""
Solution 2: Optimized code
Runtime 32 ms Beats 77.80%
Memory 16.5 MB Beats 5.10%
TC:O(n)
SC:O(1)
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        for i in range(min(m,n)):
            if s[i]!=t[i]:
                if m==n:return s[i+1:]==t[i+1:]
                elif m< n:return s[i:]==t[i+1:]
                else: return s[i+1:]==t[i:]
        return abs(m-n)==1