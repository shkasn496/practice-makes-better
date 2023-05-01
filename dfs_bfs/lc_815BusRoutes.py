# https://leetcode.com/problems/bus-routes/description/
"""
Solution 1: BFS : 
    - Create adjacency of station -> buses going through station
    - store a tracked_buses set to track the bus being taken
    - use bfs queue to start from source station with buses_taken=0
    - for the buses that pass through station, only choose the bus route
    - that has not been taken yet

Runtime 652 ms Beats 32.79%
Memory 48.5 MB Beats 30.28%

TC: O(N^2)
SC:O(N^2)
"""
from queue import Queue
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:return 0
        # create station -> buses graph
        graph = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for station in route:
                graph[station].add(bus)
        if source not in graph or target not in graph:return -1
        queue = Queue()
        queue.put((source,0))
        tracked_buses = set()#visited buses
        while not queue.empty():
            station, buses_taken = queue.get()
            if station==target:
                del graph, queue, tracked_buses
                return buses_taken
            for bus in graph[station]:
                if bus not in tracked_buses:
                    tracked_buses.add(bus)
                    for s in routes[bus]:
                        queue.put((s, buses_taken+1))
        del graph, queue, tracked_buses
        return -1