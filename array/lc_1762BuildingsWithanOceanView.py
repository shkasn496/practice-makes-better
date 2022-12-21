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