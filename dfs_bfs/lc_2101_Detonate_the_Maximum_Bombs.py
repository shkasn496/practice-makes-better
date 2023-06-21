# https://leetcode.com/problems/detonate-the-maximum-bombs/description/
"""
Solution 1: DFS. Add the bombs as directed graphs to an adjacency list if
                bomb1 can diffuse bomb2. 
                It's a directed graph because bomb1 can diffuse bomb2 does 
                not mean that bomb2 can diffuse bomb1 (Does not have commutative property)
Runtime 662 ms Beats 86.29%
Memory 17.3 MB Beats 11.81%

TC: O(n^2) + O(n)*O(n^2) ~ O(n^3)
    O(n^2) to create adjacency graph
    O(n^3) to traverse each bomb and run dfs at O(n^2)
SC :O(n^2) storing node and it's edges + recursive stack
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def euclidean_distance(x1, y1, x2, y2):
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        # create adjcancy graph of bombs
        #key = bomb_i directed edges with values : [bomb_j]
        graph = {i:set() for i in range(len(bombs))}
        for i in range(len(bombs)-1):
            x1, y1, r1 = bombs[i]
            for j in range(i+1,len(bombs)):
                x2, y2, r2 = bombs[j]
                dist = euclidean_distance(x1, y1, x2, y2)
                if dist <= r1:graph[i].add(j)
                if dist <= r2:graph[j].add(i)
        def dfs(bomb, visited):
            visited.add(bomb)
            path = 1
            for ngbr in graph[bomb]:
                if ngbr not in visited:
                    path+=dfs(ngbr, visited)
            return path
        max_detonations = 1
        for bomb in graph.keys():#these are the bombs that can be diffused
            bombs_detonated = dfs(bomb, set())
            max_detonations = max(max_detonations, bombs_detonated)
        del graph
        return max_detonations