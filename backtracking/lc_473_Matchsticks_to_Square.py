# https://leetcode.com/problems/matchsticks-to-square/description/
"""
Solution 1: Backtracking + sorting in reverse to reduce calculations of square sides
Runtime 9461 ms Beats 5.1%
Memory 16.3 MB Beats 72.22%

TC: O(nlogn + 4^n)
SC: O(n)
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        perimeter = sum(matchsticks)
        if N < 4 or perimeter % 4 != 0:return False
        side = perimeter / 4
        matchsticks.sort(reverse=True)
        def backtrack(idx=0, side1=0, side2=0, side3=0, side4=0):
            # 1. Conditions
            if side1>side or side2>side or side3>side or side4>side:
                return False
            # 2. Goal
            if idx==N:return side1==side2==side3==side4==side
            # 3. Choices
            m = matchsticks[idx]
            return backtrack(idx+1, side1+m, side2, side3, side4) or \
            backtrack(idx+1, side1, side2+m, side3, side4) or \
            backtrack(idx+1, side1, side2, side3+m, side4) or \
            backtrack(idx+1, side1, side2, side3, side4+m)
        return backtrack()

"""
Solution 2: Cleaner solution, iterating over sides array. 
            Slightly faster as well.
Runtime 7184 ms Beats 35.37%
Memory 16.3 MB Beats 95.39%

TC: O(nlogn + 4^n)
SC: O(n)
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        perimeter = sum(matchsticks)
        if N < 4 or perimeter % 4 != 0:return False
        side = perimeter / 4
        matchsticks.sort(reverse=True)
        def backtrack(idx=0, sides=[0,0,0,0]):
            # 2. Goal
            if idx==N:return sum(sides)==perimeter
            # 3. Choices
            m = matchsticks[idx]
            state = False
            for s_idx in range(4):
                # 1. Conditions
                if sides[s_idx]+m>side:continue
                sides[s_idx]+=m
                state = state or backtrack(idx+1,sides)
                if state:break
                sides[s_idx]-=m # backtrack
            return state
        return backtrack()