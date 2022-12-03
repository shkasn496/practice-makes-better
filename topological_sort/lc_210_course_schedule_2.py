# https://leetcode.com/problems/course-schedule-ii/description/
"""
Solution 1: BFS Traversal Kahn's algorithm along with cycle detection

Runtime 119 ms Beats 82.10%
Memory 15.6 MB Beats 59.57%

TC: O(n+e) 
SC : O(n)
"""
from queue import Queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==1 and len(prerequisites)==0:return [0]
        graph, indegree = self.create_adj_list_and_indegree(numCourses, prerequisites)
        queue = Queue()
        ordering=[]

        # fill queue with indegree zero nodes
        for node, degree in indegree.items():
            if degree==0: queue.put(node)
        
        while not queue.empty():
            curr_node = queue.get()
            # sorted elem
            ordering.append(curr_node)
            for ngbr in graph[curr_node]:
                indegree[ngbr]-=1
                if indegree[ngbr]==0:queue.put(ngbr)
        del graph, indegree, queue
        return ordering if len(ordering)==numCourses else []
    
    def create_adj_list_and_indegree(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            # b -> a
            indegree[a]+=1
            graph[b].append(a)
        return graph, indegree

"""
Solution 2: DFS Traversal (slightly faster for cycle detection)

Runtime 99 ms Beats 97.52%
Memory 17.2 MB Beats 40.84%

TC: O(n+e)
SC : O(n)
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==1 and len(prerequisites)==0: return [0]
        graph = self.create_adj_list(numCourses, prerequisites)
        visited, dfs_visit = set(), set()
        stack = [] # stores top sort result

        def cycleDetected(course):
            # add courses to visit and dfs visit
            visited.add(course)
            dfs_visit.add(course)
            
            # check if ngbr is present
            for ngbr in graph[course]:
                if ngbr not in visited:
                    if cycleDetected(ngbr):return True
                # if ngbr is already visited and exists in dfs_visit, it's a cycle
                elif ngbr in dfs_visit:return True
            
            # now add the course to the stack call
            stack.append(course)

            # remove course from dfs visit since it's not part of cycle
            dfs_visit.remove(course)
            return False

        for course in range(numCourses):
            if course not in visited:
                if cycleDetected(course):return []
        
        del graph, visited, dfs_visit
        if len(stack)!=numCourses:return []
        return [stack.pop() for _ in range(numCourses)] 

    def create_adj_list(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        return graph