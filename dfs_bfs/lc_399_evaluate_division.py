# https://leetcode.com/problems/evaluate-division/description/
"""
Solution 1: BFS
Runtime 21 ms Beats 99.28%
Memory 14.1 MB Beats 8.78%
TC: O(M*N) N=len(equations), M=len(values)
SC: O(N+M) to store result
    O(N) for graph, visited, queue
"""
from queue import Queue
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.create_adjacency_list(equations, values)
        output=[]

        # using bfs to find shortest path from start node to end node
        def bfs(start_node, end_node):
            visited=set()
            queue=Queue()
            queue.put((start_node, 1.0))
            while not queue.empty():
                node, value = queue.get()
                if node==end_node:return value
                visited.add(node)
                for ngbr in graph[node]:
                    if ngbr in visited:continue
                    queue.put((ngbr,value*graph[node][ngbr]))
            del visited, queue
            return -1.0 #return -1 if no path found

        # run through the queries
        for a,b in queries:
            if a not in graph or b not in graph: #check if variables aren't present
                output.append(-1.0)
            elif a==b:output.append(1.0) #check if variable is divided by itself
            else:output.append(bfs(a,b)) #check for chain rule path from start to end nodes
        del graph
        return output

    # create dict of dict to store directed paths from variables
    def create_adjacency_list(self, equations, values):
        graph = {}
        for (a, b), value in zip(equations, values):
            if a not in graph:graph[a]={}
            if b not in graph:graph[b]={}
            graph[a][b]=value
            graph[b][a]=float(1/value)
        return graph

"""
Solution 2 : DFS
Runtime 44 ms Beats 76.79% 
Memory 16.5 MB Beats 28.10%
TC: O(M*N) N=len(equations), M=len(values)
SC: O(N+M) to store result
    O(N) for  visited, recursive stack
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b]=val
            graph[b][a]=float(1/val)
        def dfs(start_node, end_node, path, visited):
            visited.add(start_node)
            ngbrs = graph[start_node]
            ret = -1.0
            if end_node in ngbrs:return path*ngbrs[end_node]
            else:
                for node, val in ngbrs.items():
                    if node in visited:continue
                    ret = dfs(node, end_node, path*val, visited)
                    if ret != -1.0:break
            del visited
            return ret
        result = []
        for a, b in queries:
            if a not in graph or b not in graph:result.append(-1.0)
            elif a==b:result.append(1.0)
            else:result.append(dfs(a,b, 1.0, set()))
        del graph
        return result