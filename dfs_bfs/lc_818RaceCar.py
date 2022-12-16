# https://leetcode.com/problems/race-car/description/
"""
Solution 1: BFS Solution

TC: O(T*log(T))
SC: O(T*log(T))
"""
from queue import Queue
class Solution:
    def racecar(self, target: int) -> int:
        if target==1: return 1
        queue = Queue()
        queue.put((0, 0, 1)) #moves, position, speed
        visited = set() # track the position and speed

        while not queue.empty():
            moves, position, speed = queue.get()
            if position==target:return moves
            if (position, speed) in visited: continue
            visited.add((position, speed))
            queue.put((moves+1, position+speed, speed*2)) # accelerate
            if (position+speed > target and speed > 0) or \
            (position+speed < target and speed < 0): #reverse
                speed = -1 if speed > 0 else 1
                queue.put((moves+1, position, speed))
        del queue, visited
        return moves