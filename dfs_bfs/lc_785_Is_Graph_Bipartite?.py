# https://leetcode.com/problems/is-graph-bipartite/description/
"""
TC: O(n+e)
SC:O(n)
"""
from queue import Queue
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        queue = Queue()
        visited = [0]* n # mark 1 as odd, -1 as even sets
        def bfs(start_node):
            if visited[start_node] != 0: return True
            queue.put((start_node, -1)) # node 0 is in even set
            while not queue.empty():
                node, set_type = queue.get()
                visited[node] = set_type
                for ngbr in graph[node]:
                    if visited[ngbr] == 0:
                        # unvisited node
                        queue.put((ngbr, set_type * (-1)))
                    else:
                        if visited[ngbr] == set_type:
                            return False
            return True
        for i in range(n):
            if bfs(i) == False:
                return False
        del visited, queue
        return True