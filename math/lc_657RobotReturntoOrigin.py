# https://leetcode.com/problems/robot-return-to-origin/description/
"""
Solution 1: Recursive solution

TC:O(n)
SC:O(n) recursive stack space
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves)==1:return False
        directions = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
        def dfs(i,prev_x, prev_y):
            x, y = directions[moves[i]]
            prev_x+=x
            prev_y+=y
            if i==len(moves)-1:
                return (prev_x,prev_y)==(0,0)
            return dfs(i+1,prev_x, prev_y)
        return dfs(0,0,0)

"""
Solution 2: Space optimization
Runtime 55 ms Beats 56.90%
Memory 16.4 MB Beats 11.28%
TC:O(n)
SC:O(1) # considering count to just hold 4 variables
"""
from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        return count['U']==count['D'] and count['L']==count['R']