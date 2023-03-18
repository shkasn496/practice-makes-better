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