# https://leetcode.com/problems/longest-palindromic-substring/description/
"""
Solution 1: Brute Force:
Iterate over every pair of characters (taking O(n^2) TC) and call isPalindrome (taking O(n)) time each call

TC: O(n^3)
SC: O(1)
"""

"""
Solution 2: 

Runtime 500 ms Beats 91.21%
Memory 13.8 MB Beats 90.11%

TC: O(n^2)
SC: O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2 :return s

        def isPalindrome(left, right):
            while left >=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1

        maxlength=start_idx = 0
        for i in range(len(s)):
            odd_palindrome_len=isPalindrome(i,i)# check odd max palindrome with center at i
            even_palindrome_len=isPalindrome(i,i+1)# check even max palindrome with center at i and i+1

            new_max_length=max(odd_palindrome_len, even_palindrome_len)
            if new_max_length> maxlength: # we only want to capture the first instance of new length
                maxlength=new_max_length
                start_idx=i-(maxlength)//2 if maxlength%2 else (i-(maxlength)//2)+1

        return s[start_idx:start_idx+maxlength]