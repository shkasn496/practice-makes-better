# https://leetcode.com/problems/reducing-dishes/description/
"""
Solution 1: Best Solution with Greedy approach and using prefix sum concept
Runtime 40 ms Beats 76.51%
Memory 16.3 MB Beats 14.76%
TC: O(nlogn)
SC:O(1)
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0]<=0:return 0
        N = len(satisfaction)
        result = 0
        prefix_sum = 0
        for i in range(N):
            prefix_sum+=satisfaction[i]
            if prefix_sum<0:break
            result+=prefix_sum
        return result

"""
Solution 2: Greedy
Runtime 156 ms Beats 18.50%
Memory 16.5 MB Beats 14.26%
TC; O(n^2)
SC:O(1)
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0]<=0:return 0
        N = len(satisfaction)
        result = satisfaction[0]
        for i in range(N):
            like_time = 0
            for t in range(i+1,0,-1): #len(window)=i+1
                like_time+=satisfaction[i+1-t]*t
            if like_time<0:break
            result=max(result, like_time)
        return result

"""
Solution 3: DFS + Memoization (Top Down Dynamic Programming)
Runtime 1035 ms Beats 5.1%
Memory 186.7 MB Beats 5.8%
TC: O(n^2)
SC: O(n^2)
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1]<=0:return 0
        N = len(satisfaction)
        dp = {}
        def dfs(idx, t):
            if idx==N:return 0
            if (idx, t) in dp:return dp[(idx,t)]
            choice1=satisfaction[idx]*t+dfs(idx+1,t+1)
            choice2=dfs(idx+1,t)
            like_time = max(choice1,choice2)
            dp[(idx,t)]=like_time
            return dp[(idx,t)]
        return dfs(0,1)