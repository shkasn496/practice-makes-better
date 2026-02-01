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
        if n < 2: return 0
        prefix_suffix_max = [0] * n # store left and right max at each index
        # get left max
        for i in range(n):
            if i==0:
                prefix_suffix_max[i] = height[i]
            else:
                prefix_suffix_max[i] = max(height[i], prefix_suffix_max[i-1])
        # get right max
        for i in range(n-1, -1, -1):
            if i==n-1:
                prefix_suffix_max[i] = min(height[i], prefix_suffix_max[i])
            else:
                prefix_suffix_max[i] = min(max(height[i], prefix_suffix_max[i+1]), prefix_suffix_max[i])
        total_rain_water = 0
        for i in range(n):
            curr_ht = height[i]
            border_ht = prefix_suffix_max[i]
            unit_rain_water = border_ht - curr_ht
            if unit_rain_water > 0:
                total_rain_water += unit_rain_water
        del prefix_suffix_max
        return total_rain_water

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