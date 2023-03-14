# https://leetcode.com/problems/valid-palindrome-ii/description/
"""
Solution 1: Using a helper function that skips a wrong element
Runtime 145 ms Beats 60.74%
Memory 14.4 MB Beats 99.58%
TC:O(n)
SC:O(1)
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)<=2:return True
        i1, i2 = 0, len(s)-1
        def checkPalindrome(i,j):
            while i<=j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:return False
            return True
        while i1<=i2:
            if s[i1]==s[i2]:
                i1+=1
                i2-=1
            else:
                return checkPalindrome(i1, i2-1) or checkPalindrome(i1+1,i2)
        return True