# https://leetcode.com/problems/time-based-key-value-store/description/
"""
Solution 1: Using Hashmap and orderedDict
Runtime 607 ms Beats 99%
Memory 72.7 MB Beats 6.48%

- init:
    TC: O(1)
    SC: O(1)
- set:
    TC: O(1)
    SC: O(N)
- get:
    TC: O(K) where K=max(len(values) of key)
    SC: O(1)

"""
import collections
class TimeMap:

    def __init__(self):
        self.timemap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=collections.OrderedDict()
        self.timemap[key][timestamp]=value
        return
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap :return ""
        i=0
        for time_prev, value in reversed(self.timemap[key].items()):
            if i==0 and timestamp>time_prev or\
            time_prev<=timestamp:return value
            i+=1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)