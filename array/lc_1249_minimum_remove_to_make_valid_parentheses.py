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
        stack=[]
        output=list(s)
        for i, c in enumerate(s):
            if c=='(':stack.append(i)
            elif c==')':
                if stack and s[stack[-1]]=='(':stack.pop()
                else:stack.append(i)
        while stack:
            output[stack.pop()]=''
        del stack
        return "".join(output)