# https://leetcode.com/problems/minimum-knight-moves/
"""
Solution 1: Using BFS traverse 8 directions and find min path

Gives TLE for this question.

TC:O(max(x,y)^2)
SC:O(max(x,y)^2)
"""
from queue import Queue
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x,y)==(0,0):return 0
        # top, down, right, left
        knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        queue = Queue()
        queue.put((0,0,0))
        visited = set()
        min_moves = 0
        while not queue.empty():
            x1, y1, moves = queue.get()
            if (x1,y1) == (x,y):
                min_moves = moves
                break
            visited.add((x1,y1))
            for dx, dy in knight_moves:
                x2, y2 = x1+dx, y1+dy
                if (x2,y2) in visited:continue
                queue.put((x2, y2, moves+1))
        del queue, knight_moves, visited
        return min_moves 

"""
Solution 2: Optimized DFS solution using symmetry property and only moving in 2 directions
            towards (0,0).
            Symmetry property: Distance is same for any direction in abs(x, y)
            Hence, start from (abs(x), abs(y)) and move in directions (-2,-1) and (-1,-2)
            to reach (0,0).
            Keep in mind 3 base cases, 
            1. When (x1,y1) == (0,0):return 0
            2. When (x1+y1==2):return 2 for base cases (1,1), (0,2), (2,0) because it takes 2
                steps to reach that point
            3. If (x1,y1) has already been visited: return min steps found at that point.

Runtime 51 ms Beats 97.26%
Memory 18.1 MB Beats 89.32%

TC:O(abs(x*y))
SC:O(abs(x*y))
"""
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dp = {}
        def dfs(x1,y1):
            if (x1,y1) in dp:return dp[(x1,y1)]
            elif (x1,y1)==(0,0):return 0
            elif x1+y1==2:return 2 # base case (1,1), (0,2),(2,0)
            dp[(x1,y1)]=min(dfs(abs(x1-2), abs(y1-1)), dfs(abs(x1-1), abs(y1-2)))+1
            return dp[(x1,y1)]
        return dfs(abs(x), abs(y))