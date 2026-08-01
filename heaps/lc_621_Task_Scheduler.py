# https://leetcode.com/problems/task-scheduler/description

"""
TC: O(n * m) where n = len(task), m = len(idleTime)

"""
import heapq
from queue import Queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = [-c for c in Counter(tasks).values()] # -count
        heapq.heapify(maxheap)
        queue = Queue() # -count, idleTime
        time = 0
        while maxheap or not queue.empty():
            time += 1
            if maxheap:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    queue.put((count, time + n))
            if not queue.empty() and queue.queue[0][1] == time:
                count, idletime = queue.get()
                heapq.heappush(maxheap, count)
        del maxheap, queue
        return time