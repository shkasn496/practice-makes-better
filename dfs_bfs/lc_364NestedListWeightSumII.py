# https://leetcode.com/problems/nested-list-weight-sum-ii/description/
"""
Solution 1: DFS
Runtime 41 ms Beats 44%
Memory 16.7 MB Beats 18%
TC: O(n)
SC: O(n)
"""
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.max_depth = 0
        def dfs(nested_list, depth):
            output = []
            if not nested_list:return output
            for nl in nested_list:
                if nl.isInteger():
                    output.append((nl.getInteger(), depth))
                else:
                    output.extend(dfs(nl.getList(), depth+1))
            self.max_depth = max(depth, self.max_depth)
            return output
        integers_and_depths = dfs(nestedList, 1)
        output = 0
        for integer, depth in integers_and_depths:
            weight = self.max_depth - (depth) + 1
            output+= (integer * weight)
        del integers_and_depths
        return output

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
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """