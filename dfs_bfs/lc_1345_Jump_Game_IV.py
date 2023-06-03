# https://leetcode.com/problems/jump-game-iv/description/
"""
Solution 1: BFS + hashmap to store indexes of same elements
Runtime 1682 ms Beats 9.26%
Memory 31.6 MB Beats 35.22%

TC:O(N)
SC:O(N)
"""
from queue import Queue
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr)==1:return 0
        if arr[0]==arr[-1]:return 1
        elem_indexes = collections.defaultdict(list)
        for i,a in enumerate(arr):
            elem_indexes[a].append(i)
        visited=set()
        queue = Queue()
        queue.put((0,0))#index, jumps
        while not queue.empty():
            index, jumps = queue.get()
            if index==len(arr)-1:
                del elem_indexes, queue, visited
                return jumps
            for next_idx in elem_indexes[arr[index]]:
                if next_idx in visited:continue
                visited.add(next_idx)
                queue.put((next_idx,jumps+1))
            del elem_indexes[arr[index]]#to not get TLE and not return to same elem
            for next_idx in [index+1, index-1]:
                if 0<=next_idx<len(arr) and next_idx not in visited:
                    visited.add(next_idx)
                    queue.put((next_idx,jumps+1))
        del elem_indexes, queue, visited
        return 0