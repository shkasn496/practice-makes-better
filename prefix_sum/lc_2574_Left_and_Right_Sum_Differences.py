class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return [0]
        n = len(nums)
        result = [0] * n
        for i in range(n-2, -1, -1):
            result[i] = result[i+1] + nums[i+1]
        leftsum = 0
        for i in range(n):
            if i==0:
                leftsum += nums[i]
                continue
            result[i] = abs(leftsum - result[i])
            leftsum += nums[i]
        return result

"""
Solution 2: STart from left
"""

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return [0]
        n = len(nums)
        result = [0]*n
        leftsum = 0
        for i in range(n):
            result[i] += leftsum
            leftsum += nums[i]
        rightsum = 0
        for i in range(n-1, -1, -1):
            result[i] = abs(result[i] - rightsum)
            rightsum += nums[i]
        return result