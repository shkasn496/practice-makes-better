# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
"""
Solution 1: Sort by end points. Update arrow count if s2 > e1 and then e1 = e2
Runtime 1062 ms Beats 98.70%
Memory 62.7 MB Beats 73.7%
TC: O(n) + O(nlogn)
SC: O(1)
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        points.sort(key = lambda point: point[1]) # sort by x_end
        arrow = 1
        e1 = points[0][1]
        for s2, e2 in points[1:]:
            if s2 > e1:
                arrow += 1
                e1 = e2
        return arrow