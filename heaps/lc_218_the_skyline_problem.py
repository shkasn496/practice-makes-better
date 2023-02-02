# https://leetcode.com/problems/the-skyline-problem/description/
"""
Solution 1: Using maxheap and also clever sorting
Runtime 1925 ms Beats 11.64%
Memory 19 MB Beats 91.62%

TC: O(nlogn) + less than O(n) for heapify inside for loop for end points
SC: O(n)
"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        coordinates=[] # store -height of start point, +height with end point for correct sorting and handling edge cases
        for l,r,h in buildings:
            coordinates.append([l,-h])
            coordinates.append([r,h])
        coordinates.sort() #this will sort -heights first followed by +heights
        maxheap=[0]#will store heights that come across at start point
        result=[]
        for x, h in coordinates:
            max_height=abs(maxheap[0])
            if h < 0: #start point
                heapq.heappush(maxheap,h)# add -h to maxheap
                if abs(h)>max_height:result.append((x,abs(h)))
            else: #end point
                maxheap.remove(-h)
                heapq.heapify(maxheap) # we need to heapify as we removed an element from somewhere in the maxheap
                if abs(h)>abs(maxheap[0]):result.append((x,abs(maxheap[0])))
        del coordinates,maxheap
        return result