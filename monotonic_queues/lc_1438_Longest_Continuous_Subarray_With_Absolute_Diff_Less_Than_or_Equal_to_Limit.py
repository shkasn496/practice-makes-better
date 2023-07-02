# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
"""
Brute Force Solution : 
Use sliding window to keep check of start and end of windows and find
max and min elements in the window.
TC: O(n2)
SC:O(1)
"""

"""
Solution : Use 2 monotonic queues, minQ and maxQ to hold min and max values indexes
- Monotonic queues allow pop operations at 0 and n-1 index positions for O(1) time complexity. 
- PS: Cannot use Queue DS as it pushes and pops only from 0th index. 
        Deque satisfies the above condition.

- Check if minQ last element is greater than current num: then pop minQ last element
- Check if maxQ last element is less than current num: then pop maxQ last element
- Add current nums to both queues
- while the max difference is greater than the limit:
    - now we will remove values from both the queues that are equal to num at start index
    - if 0th element at minQ is equal to num at start idx, popLeft() the 0th element
    - if 0th element at maxQ is equal to num at start idx, popLeft() the 0th element
    - increment the start pointer which is holding the sliding window interval

- finally, check the current sliding window size against max sliding window size.

Runtime 628 ms Beats 84.45% 
Memory 25.7 MB Beats 91.3%
TC: O(N)
SC:O(N)
"""
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums)<2:return 1
        max_size = 0
        start=0
        # create two monotonic increasing queues to store min and max values
        minQ, maxQ = deque(), deque()
        for j, num in enumerate(nums):
            while minQ and minQ[-1] > num:
                minQ.pop()
            while maxQ and maxQ[-1] < num:
                maxQ.pop()
            minQ.append(num)
            maxQ.append(num)
            while maxQ[0] - minQ[0] > limit:
                if minQ[0] == nums[start]: minQ.popleft()
                if maxQ[0] == nums[start]: maxQ.popleft()
                start+=1
            max_size = max(max_size, j - start + 1)
        del minQ, maxQ
        return max_size

#### if you want to store indexes in the queues instead of nums, below solution will work.
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums)<2:return 1
        max_size = 0
        start=0
        # create two monotonic increasing queues to store min and max value indexes
        minQ, maxQ = deque(), deque()
        for j, num in enumerate(nums):
            while minQ and nums[ minQ[-1] ] > num:
                minQ.pop()
            while maxQ and nums[ maxQ[-1] ] < num:
                maxQ.pop()
            minQ.append(j)
            maxQ.append(j)
            while nums[ maxQ[0] ] - nums[ minQ[0] ] > limit:
                start+=1
                if minQ[0] < start: minQ.popleft()
                if maxQ[0] < start: maxQ.popleft()
            max_size = max(max_size, j - start + 1)
        del minQ, maxQ
        return max_size