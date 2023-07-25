# https://leetcode.com/problems/k-closest-points-to-origin/description/
"""
Solution 1: Min heap
Runtime 811 ms Beats 65.83%
Memory 22.5 MB Beats 74.36%

TC: O(n)+ O(klogk)
SC:O(n)
"""
import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [] # store point idx based on distance
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            euc_dist = math.sqrt((x1)**2 + (y1)**2)
            minheap.append((euc_dist, i))
        heapq.heapify(minheap)
        return [points[heapq.heappop(minheap)[1]] for _ in range(k)]

"""
Solution 2: Maxheap
Runtime 796 ms Beats 75.88%
Memory 22.2 MB Beats 94.71%

TC: O(nlogk)
SC: O(k)
"""
import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = [] # store point idx based on distance
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            euc_dist = math.sqrt((x1)**2 + (y1)**2)
            heapq.heappush(maxheap,(-euc_dist, i))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        result = [points[i] for _,i in maxheap]
        del maxheap
        return result
