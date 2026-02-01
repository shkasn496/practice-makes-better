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
        n = len(s)
        if n < 2: return s
        def get_palindrome_length(left, right):
            while left >= 0 and right < n and s[left]==s[right]:
                left -= 1
                right += 1
            return right - left - 1
        max_length = start_idx = 0
        for mid_idx in range(n):
            odd_length = get_palindrome_length(mid_idx, mid_idx)
            even_length = get_palindrome_length(mid_idx, mid_idx + 1)
            curr_length = max(odd_length, even_length)
            if curr_length > max_length:
                max_length = curr_length
                if max_length % 2 != 0: # odd
                    start_idx = mid_idx - (max_length // 2)
                else: # even
                    start_idx = mid_idx - (max_length // 2) + 1
        return s[start_idx: start_idx+max_length]


"""
 Solution 2: 2D DP solution 

 TC: O(n^2)
 SC: O(n^2)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        cache = [[False] * n for _ in range(n)]
        ans = [0, 0]
        for i in range(n):
            cache[i][i] = True
        for i in range(n-1):
            j = i + 1
            if s[i]==s[j]:
                cache[i][j] = True
                ans = [i, j]
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                if s[i]==s[j] and cache[i+1][j-1]:
                    cache[i][j] = True
                    ans = [i, j]
        del cache
        i, j = ans
        return s[i:j+1]

