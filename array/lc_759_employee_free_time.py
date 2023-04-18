# https://leetcode.com/problems/employee-free-time/description/
"""
Solution 1: Sorting and checking against end values
Runtime 78 ms Beats 95.58%
Memory 15.8 MB Beats 71.39%
TC: O(nlogK)+O(n*k) where K is max no.of intervals. 
                O(n*k) is for flattening the schedule into intervals array
SC:O(n)
"""
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flatten schedule of employees to just intervals lists
        intervals = [[interval.start, interval.end] for employee in schedule for interval in employee]
        
        # sort the list by increasing order of start interval and decreasing order of end interval
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        max_end=intervals[0][1] #storing end
        output = []
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s > max_end : #found a open interval
                output.append(Interval(start=max_end, end=s))
            max_end=max(max_end, e)
        del intervals, max_end
        return output

# not so clean code with more if conditions that are redundant
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [[interval.start, interval.end] for employee in schedule for interval in employee]
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        max_end=intervals[0][1] #storing end
        output = []
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= max_end and e <=max_end:continue
            elif s <= max_end and e > max_end:max_end=e
            elif s > max_end : #found a open interval
                output.append(Interval(start=max_end, end=s))
                max_end=e
        del intervals, max_end
        return output