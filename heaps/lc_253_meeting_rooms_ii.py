# https://leetcode.com/problems/meeting-rooms-ii/description/
"""
Solution 1: Use minheap to store end times of meeting. Store a variable
    to track the max meeting rooms in heap
Runtime 85 ms Beats 73.90%
Memory 19.9 MB Beats 51.75%
TC:O(nlogn) Sorting + heappush and heappop operations
SC: O(n) max rooms = len(intervals)
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:return 0
        intervals.sort(key=lambda interval : interval[0])
        busy_rooms=[] #place end time of first interval
        heapq.heappush(busy_rooms, intervals[0][1])
        room_count = len(busy_rooms)
        for interval in intervals[1:]:
            #if no overlap in busy_rooms
            while busy_rooms and interval[0]>=busy_rooms[0]:#if start2 > end1
                heapq.heappop(busy_rooms)
            heapq.heappush(busy_rooms, interval[1]) #if overlap
            room_count = max(room_count,len(busy_rooms))
        del busy_rooms
        return room_count