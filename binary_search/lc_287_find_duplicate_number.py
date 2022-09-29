'''
https://leetcode.com/problems/find-the-duplicate-number/
Runtime: 651 ms, faster than 95.14% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 27.9 MB, less than 57.48% of Python3 online submissions for Find the Duplicate Number.
TC: O(N), SC:O(1)
'''
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        #cycle detection using floyd's tortoise and hare algo TC:O(n), SC:O(1)
        #start point
        tortoise=hare=nums[0]
        #phase 1- hare speed = 2x tortoise. Stop when hare and tortoise meet at intersection.
        while True:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]
            if hare==tortoise:break
        #phase 2- hare speed = tortoise. Tortoise at start and hare at intersection.
        tortoise=nums[0]
        while (tortoise!=hare):
            tortoise=nums[tortoise]
            hare=nums[hare]
        return tortoise

    '''
    Alternative clever solution. Takes TC: O(nlogn), SC:O(1)
    Uses binary search
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        # left and right represent range of values present in nums
        left, right = 1, len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            count=0
            # count how many numbers are less than or equal to mid
            count = sum(num <=mid for num in nums)
            if count>mid:
                duplicate=mid
                right = mid-1
            else:left=mid+1
        return duplicate