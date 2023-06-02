# https://www.lintcode.com/problem/1862/description?_from=problem_tag&fromId=63

"""
Solution 1: BFS
2993 ms
time cost
·
31.24 MB
memory cost
·
Your submission beats
8.00 % Submissions

TC:O(n)
SC:O(n)
"""
from typing import (
    List,
)
from queue import Queue
class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
    def time_to_flower_tree(self, father: List[int], time: List[int]) -> int:
        # write your code here
        adjacency_list = collections.defaultdict(list)
        for child, parent in enumerate(father):
            if child==0:continue
            adjacency_list[parent].append(child)
        max_time = 0
        queue = Queue()
        queue.put((0,0))
        while not queue.empty():
            parent, water_time = queue.get()
            if parent not in adjacency_list:
                max_time = max(max_time, water_time)
            else:
                for child in adjacency_list[parent]:
                    queue.put((child,water_time+time[child]))
        del adjacency_list, queue, father, time
        return max_time
