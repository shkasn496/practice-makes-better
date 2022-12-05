# https://leetcode.com/problems/valid-parentheses/description/
"""

Runtime 28 ms Beats 97.39%
Memory 14 MB Beats 26.56%

TC: O(n)
SC: O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in ")]}" or len(s)% 2 != 0 : return False
        stack=[]
        mapping = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c not in mapping: #found opening bracket
                stack.append(c)
            else:
                if stack:
                    if stack[-1]==mapping[c]:
                        stack.pop()
                        continue
                return False
        return len(stack)==0