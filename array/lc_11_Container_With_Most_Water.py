# https://leetcode.com/problems/container-with-most-water/description/
"""
Solution : Create two pointers, move in the direction where height is greater, so that you can capture more area
Runtime 784 ms Beats 91.84%
Memory 26.2 MB Beats 92.24%

TC: O(n)
SC: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1 : return 0
        start,end, max_area=0, len(height)-1, 0
        while start < end:
            max_area= max(min(height[start], height[end])*abs(end-start), max_area)
            if height[start] <= height[end]:start+=1
            else:end-=1
        return max_area


# Cleaner soluton, slightly slower since calls happening to a helper function
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1 : return 0
        start,end, max_area=0, len(height)-1, 0

        def calculateArea(start_x, end_x, start_y, end_y):
            length = min(start_y, end_y)
            breath = abs(end_x-start_x)
            return length * breath

        while start < end:
            max_area= max(calculateArea(start, end, height[start], height[end]), max_area)
            if height[start] <= height[end]:
                start+=1
            else:end-=1
        return max_area