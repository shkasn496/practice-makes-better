# https://leetcode.com/problems/minimum-window-substring/description/
"""
Solution : 
TC: O(m + n)
SC : O(m+n)
"""
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ""
        t_counts = Counter(t)
        s_counts = defaultdict(int)
        l = r = matches = 0
        required_matches = len(t_counts)
        result = [float("inf"), l, r] # store length, start_idx and end idx of string
        while r < len(s):
            curr_char = s[r]
            s_counts[curr_char] += 1
            if curr_char in t_counts and s_counts[curr_char] == t_counts[curr_char]:
                matches += 1
            while l <= r and matches == required_matches:
                remove_char = s[l]
                if r - l + 1 < result[0]:
                    result = [r - l + 1, l, r]
                s_counts[remove_char] -= 1
                if remove_char in t_counts and s_counts[remove_char] < t_counts[remove_char]:
                    matches -= 1
                l += 1
            r += 1
        del t_counts, s_counts
        return s[result[1]: result[2]+ 1] if result[0] != float("inf") else ""
