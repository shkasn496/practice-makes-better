# https://leetcode.com/problems/meeting-rooms/description/
"""
Solution 1: Sort
Runtime 82 ms Beats 71.82%
Memory 19.9 MB Beats 16.30%
TC:O(nlogn)
SC:O(1)
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:return True
        intervals.sort(key=lambda elem:elem[0])
        _,e1 = intervals[0]
        for i in range(1, len(intervals)):
            s2, e2 = intervals[i]
            if e2<=e1 or s2<e1:return False
            e1 = e2
        return True