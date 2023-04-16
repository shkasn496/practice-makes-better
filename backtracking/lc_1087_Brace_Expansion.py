# https://leetcode.com/problems/brace-expansion/description/
"""
Solution 1: Backtracking
Runtime 27 ms Beats 98.98%
Memory 14.5 MB Beats 14.29%
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        if len(s)==1:return [s]
        N=len(s)
        words = []
        def backtrack(idx, sub_array):
            # 1. Conditions
            if idx > N:return
            # 2. Goal
            if idx==N:
                words.append("".join(sub_array))
                return
            # 3. Choices
            if s[idx]=='{':
                end = s.index('}', idx)
                choices = s[idx+1:end].split(',')
                for choice in sorted(choices):
                    backtrack(end+1, sub_array+[choice])
            else: backtrack(idx+1, sub_array+[s[idx]])
            return
        backtrack(0,[])
        return words