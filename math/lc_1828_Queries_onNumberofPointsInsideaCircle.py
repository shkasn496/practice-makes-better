# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/
"""
Solution 1: Using circle equation
Runtime 2657 ms Beats 13.32%
Memory 14.1 MB Beats 99.13%
TC:O(N*Q) where Q is the queries and N is len of points
SC:O(1) as no additional space was used. O(Q) to store the output
"""
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def circle_equation(x,y,x1,y1,r):
            circle = (x-x1)**2 + (y-y1)**2
            return 1 if circle <= r**2 else 0
        output = [0]*len(queries)
        for i, (x,y,r) in enumerate(queries):
            for (x1,y1) in points:
                output[i] += circle_equation(x,y,x1,y1,r)
        return output