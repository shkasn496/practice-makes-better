# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
"""
Solution: Using stack
Runtime 70 ms Beats 98.38%
Memory 15.6 MB Beats 73.83%
TC: O(n)
SC:O(n)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        if not n : return s
        stack = [] # only store indexes of parenthesis that either will match or will be replaced with ""
        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(idx)
        ans = list(s)
        while stack:
            ans[stack.pop()]= "" # replace incomplete parentheses with ""
        return "".join(ans)