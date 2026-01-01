# https://leetcode.com/problems/course-schedule/description/
"""
Solution 1: BFS - using Kahn's algorithm Topo Sort

TC : O(n + e)
SC : O(n)
"""
from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i : [] for i in range(numCourses)}
        indegrees = [0] * numCourses
        for a,b in prerequisites:
            # b->a
            adj_list[b].append(a)
            indegrees[a]+=1
        queue = Queue()
        topo_sort = 0
        for course, deg in enumerate(indegrees):
            if deg==0:
                queue.put(course)
        while not queue.empty():
            course = queue.get()
            topo_sort += 1
            for ngbr in adj_list[course]:
                indegrees[ngbr] -= 1
                if indegrees[ngbr] == 0:
                    queue.put(ngbr)
        del adj_list, indegrees, queue
        return topo_sort == numCourses   

"""
Solution 2: Using DFS for directed graphs, search for presence of cycle

TC: O(n+e)
SC : O(n)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        cycle Detection on directed graph. Using dfs
        TC: O(n+e), SC:o(n)
        '''
        if len(prerequisites) < 1: return True
        graph = self.createAdjList(numCourses, prerequisites)
        visited={n: 0 for n in range(numCourses)} #unvisited=0, visiting/cycle= -1, visited=1
        def dfs_helper(node):
            if visited[node] in [-1,1]: return visited[node]==1
            #currently visiting the node
            visited[node]=-1
            for ngbr in graph[node]:
                if not dfs_helper(ngbr):return False
            #successfully visited
            visited[node]=1
            return True
            
        state=True
        for n in range(numCourses):
            if visited[n] ==0:
                state &= dfs_helper(n)
                if not state: return state
        del visited, graph
        return state        
        
    def createAdjList(self, numCourses, prereqs):
        graph = {n: [] for n in range(numCourses)}
        for course, prereq in prereqs:
            graph[prereq].append(course)
        return graph