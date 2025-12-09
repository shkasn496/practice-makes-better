# https://leetcode.com/problems/merge-intervals/description/
"""
Solution 1: Sort the array, then check for overlapping intervals
Runtime 138 ms Beats 96.87%
Memory 18.9 MB Beats 21.62%
TC: O(nlogn) + O(n) # sorting + linear search through interval
SC:O(n)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:return intervals
        intervals.sort()
        output=[intervals[0]]
        for i in range(1,len(intervals)):
            s1, e1 = output[-1]
            s2, e2 = intervals[i]
            if e1-s2>=0:#overlap
                if e2<=e1:#completely inbound
                    continue
                output[-1]=[s1,e2]
            else:#no overlap
                output.append([s2,e2])
        return output
    
"""
Solution 2: Same logic, just comparing 
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals
        intervals.sort()
        result = [intervals[0]]
        for s2, e2 in intervals[1:]:
            s1, e1 = result[-1]
            if e1 <= s2:
                if e1 == s2: # extend start and end range
                    result[-1] = [s1, e2]
                else: # no overlap
                    result.append([s2, e2])
            elif s2 < e1:
                if e2 >= e1: # only add if e2 is greater
                    result[-1] = [s1, e2]
        return result