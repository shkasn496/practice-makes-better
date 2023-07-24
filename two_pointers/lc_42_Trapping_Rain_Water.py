# https://leetcode.com/problems/trapping-rain-water/description/
"""
Solution 1: Using cache to store max left heights and max right heights
Runtime 148 ms Beats 34.39% 
Memory 18.7 MB Beats 33.83%
TC:O(n)
SC:O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==1:return 0
        left_height, right_height = [height[0]], [height[n-1]]
        for h in height[1:]:
            left_height.append(max(h, left_height[-1]))
        for h in reversed(height[:n-1]):
            right_height.append(max(h, right_height[-1]))
        right_height = list(reversed(right_height))
        trapped_rain_water = 0
        for i in range(n):
            trapped_rain_water+=min(left_height[i], right_height[i])-height[i]
        del left_height, right_height
        return trapped_rain_water

"""
Solution 2: (Optimized in space) Using two pointers and variables to hold 
            max left and max right heights at each iteration
Runtime 118 ms Beats 97.65%
Memory 18.1 MB Beats 99.21%
TC:O(n)
SC:O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==1:return 0
        left, right = 0, n-1
        left_height, right_height = height[0], height[n-1]
        trapped_rain_water=0
        while left <= right:
            if left_height < right_height:
                # cannot trap water at current left step
                if height[left] > left_height:
                    left_height=height[left]
                # can trap water at current left step
                else:
                    trapped_rain_water+=left_height-height[left]
                    left+=1
            else:
                # cannot trap water at current right step
                if height[right] > right_height:
                    right_height=height[right]
                # can trap water at current right step
                else:
                    trapped_rain_water+=right_height-height[right]
                    right-=1
        return trapped_rain_water