# https://leetcode.com/problems/nested-list-weight-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
"""
Solution 1: BFS
TC: O(N) where N are the total nested list elements
SC: O(N) worst case is if all the list elements are nested integers
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from queue import Queue
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        n = len(nestedList)
        queue = Queue()
        for elem in nestedList:
            queue.put((elem, 1))
        weighted_sum = 0
        while not queue.empty():
            elem, depth = queue.get()
            if elem.isInteger():
                weighted_sum += elem.getInteger() * depth
            else: # nestedlist:
                for child in elem.getList():
                    queue.put((child, depth + 1))
        del queue
        return weighted_sum