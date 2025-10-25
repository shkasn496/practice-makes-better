# https://leetcode.com/problems/valid-palindrome/description/
"""
Solution 1: Filtering string then match with reverse
Runtime 35 ms Beats 96.85%
Memory 20.2 MB Beats 5.21%
TC:O(n)
SC:O(n)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        text=[c.lower() for c in s if c.isalpha() or c.isdigit()]
        return text==list(reversed(text))

"""
Solution 2: Using two pointers (Space efficient)
Runtime 44 ms Beats 78.80%
Memory 14.6 MB Beats 95.74%
TC: O(n)
SC:O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():l+=1
            while l < r and not s[r].isalnum():r-=1
            if l < r and s[l].lower() != s[r].lower():return False
            l+=1
            r-=1
        return True

"""
Solution 3: Simple helper with palindrome check happening from 
            inside out
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        s = [c.lower() for c in s if c.isalnum()] # clean up the string
        mid = len(s)//2
        return self.palindrome_checker(s, mid-1, mid) if len(s) % 2 == 0 else \
        self.palindrome_checker(s, mid, mid)

    def palindrome_checker(self, s, left, right):
        while 0 <= left <= right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                return False
        return True