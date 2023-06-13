# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""
Solution 1: It's O(1) to search for values and their indexes in a dict.
            It's O(1) to swap elems in a list and pop off last elem from a list.
Runtime 363 ms Beats 97.54%
Memory 63.8 MB Beats 28.31%

TC:O(1) for all functions
SC:O(n) for dict and list
"""
import random
class RandomizedSet:

    def __init__(self):
        self.elems = dict()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.elems:return False
        self.elems[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elems:return False
        # move the elem to the last position to pop out of list
        idx = self.elems[val]
        last_elem = self.list[-1]
        self.list[-1], self.list[idx]= self.list[idx], self.list[-1]#swap elems
        # update indexes in dict
        self.elems[last_elem]=idx
        del self.elems[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()