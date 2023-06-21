# https://leetcode.com/problems/parallel-courses/description/
"""
Solution 1: Topological sorting Using Kahns algorithm BFS traversal,
            check for cycle, 
            increment semester count only once per level traversal
Runtime 300 ms Beats 20.12%
Memory 20.2 MB Beats 49.13%
TC:O(n+e) where e are the no. of edges determined by relations array. 
SC:O(n+e) 
"""
from queue import Queue
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i:[] for i in range(1, n+1)}
        indegree = {i:0 for i in range(1, n+1)}
        for prev, nxt in relations:
            graph[prev].append(nxt)
            indegree[nxt]+=1
        queue = Queue()
        for node, degree in indegree.items():
            if not degree:queue.put(node)
        semesters = 0
        classes_taken=0
        while not queue.empty():
            semesters +=1 # semester must only increase once per level
            level = queue.qsize()
            for _ in range(level):
                node = queue.get()
                classes_taken +=1 # top sort val increases class count
                for ngbr in graph[node]:
                    indegree[ngbr]-=1
                    if not indegree[ngbr]:
                        queue.put(ngbr)
        del graph, indegree, queue
        return semesters if classes_taken == n else -1