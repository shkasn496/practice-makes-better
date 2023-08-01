# https://leetcode.com/problems/buildings-with-an-ocean-view/description/
"""
Solution : Iterate through array from right to left i.e from closest to ocean to farthest from ocean
Runtime 672 ms Beats 98.90%
Memory 31.1 MB Beats 87.25%
TC: O(n)
SC: O(n)
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output=[len(heights)-1]
        for i in range(len(heights)-2, -1,-1):
            if heights[i]>heights[output[-1]]:output.append(i)
        return reversed(output)

"""
Solution 1.b : Using max height
Runtime 550 ms Beats 99.46%
Memory 33.3 MB Beats 96.23%
TC:O(n)
SC:O(n)
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        max_height = heights[n-1]
        result = [n-1]
        for idx in range(n-2, -1, -1):
            h = heights[idx]
            if h > max_height:
                result.append(idx)
                max_height=h
        return reversed(result)

"""
Solution 2: If you have to traverse left to right, use a stack
Runtime 579 ms Beats 95.83%
Memory 34.2 MB Beats 5.25%
TC:O(n)
SC:O(n)
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        for idx in range(n):
            while stack and heights[stack[-1]]<=heights[idx]:
                stack.pop()
            stack.append(idx)
        return stack