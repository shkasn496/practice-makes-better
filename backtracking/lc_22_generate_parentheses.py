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

"""
Solution 2: Cleaner code for backtracking
TC=SC=O(n*(2^2n))=O(n*(4^n))

The recursion tree in this problem is a binary tree where vertices 
represent incomplete sequences of brackets and edges represent the 
choice of the next bracket (either left or the right). 
The height of the tree is 2n, since we must branch once per bracket. 
So the number of vertices is at most 2^2n and the number of leaves 
is at most half the number of vertices of a perfect tree, 
so asymptotically O(2^2n). Additionally we do linear work per leaf 
to copy the sequence to output.

A more complete analysis would take into account that some bracket 
choices are invalid, which leads to asymptotically fewer leaves in the tree. 
However since we are interested in upper bounds, it's still correct 
to say that time complexity is O(n*(2^2n)), even though it's not 
the most accurate upper bound.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:return []
        combinations = []
        def backtrack(open_brackets, close_brackets, subarray):
            # 1. Conditions
            if open_brackets<close_brackets or len(subarray)>2*n:return
            # 2. Goal
            if open_brackets==close_brackets and len(subarray)==2*n:
                combinations.append("".join(subarray))
                return
            # 3. Choices
            if open_brackets < n:
                backtrack(open_brackets+1, close_brackets, subarray+['('])
            if close_brackets < open_brackets:
                backtrack(open_brackets, close_brackets+1, subarray+[')'])
        backtrack(0,0,[])
        return combinations