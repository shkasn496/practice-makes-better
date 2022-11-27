# https://leetcode.com/problems/generate-parentheses/description/
"""
Runtime 28 ms Beats 99.17%
Memory 14.3 MB Beats 41%
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def recurse (start, end, substring):
            # conditions
            if start <0 or end <0 or start > end: return
            # goal
            if start == end == 0:
                output.append(substring)
                return
            # choice 1: add an open parenthesis
            recurse(start-1, end, substring+"(")
            # choice 2: add a closed parenthesis
            recurse(start, end-1, substring+")")
            return
        recurse(n,n, "")
        return output