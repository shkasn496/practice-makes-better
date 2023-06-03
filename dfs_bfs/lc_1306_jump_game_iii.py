# https://leetcode.com/problems/jump-game-iii/description/
"""
Solution 1: BFS traversal. Slower than DFS as I'm traversing multiple
            sub paths by level, but for this Question, I need to return
            true if there is zero val in any path.
Runtime 517 ms Beats 5.4%
Memory 23 MB Beats 80.95%
TC:O(n)
SC:O(n) for queue
"""
from queue import Queue
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0:return True
        found_zero=False
        queue = Queue()
        queue.put((start, arr[start])) # index and jump val
        while not queue.empty():
            index, jump = queue.get()
            if arr[index]==0:
                found_zero=True
                break
            if arr[index]<=0:continue #visited already
            arr[index]*= -1 #mark as visited

            jump_right_idx = index+jump
            if 0<=jump_right_idx<len(arr):
                queue.put((jump_right_idx, arr[jump_right_idx]))

            jump_left_idx = index-jump
            if 0<=jump_left_idx<len(arr):
                queue.put((jump_left_idx, arr[jump_left_idx]))
        del queue
        return found_zero

"""
Solution 2: DFS (Faster solution even if worst case TC same as BFS)
Runtime 289 ms Beats 90.11%
Memory 69.7 MB Beats 27.29%

TC:O(n)
SC:O(n) recursive stack
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0:return True
        def dfs(idx):
            if not 0<=idx<len(arr) or arr[idx]<0:return False
            if arr[idx]==0:return True
            arr[idx]*=-1#mark as visited
            return dfs(idx+arr[idx]) or dfs(idx-arr[idx])
        return dfs(start)