# https://leetcode.com/problems/palindrome-partitioning/
"""
Solution : Backtrack + DP 

TC & SC: O(n * 2^N)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1: return [[s]]
        n = len(s)
        cache = {}
        result = []
        def is_palindrome(start_idx, end_idx):
            if start_idx == end_idx: return True
            if (start_idx, end_idx) in cache:
                return cache[(start_idx, end_idx)]
            while start_idx < end_idx:
                if s[start_idx] != s[end_idx]:
                    cache[(start_idx, end_idx)] = False
                    return cache[(start_idx, end_idx)]
                start_idx += 1
                end_idx -= 1
            cache[(start_idx, end_idx)] = True
            return cache[(start_idx, end_idx)]
        def backtrack(start_idx, substring):
            if start_idx == n:
                result.append(substring)
                return
            for end_idx in range(start_idx, n):
                if is_palindrome(start_idx, end_idx):
                    backtrack(end_idx + 1, substring + [s[start_idx: end_idx + 1]])
            return
        backtrack(0, [])
        del cache
        return result