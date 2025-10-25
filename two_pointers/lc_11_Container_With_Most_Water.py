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

"""
Solution 1.b: Same code logic
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==2: return min(height)**2
        max_area = 1
        left, right = 0, len(height)-1
        while left < right:
            container_height = min(height[left], height[right])
            container_width = right - left
            max_area = max(max_area, container_width * container_height)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
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