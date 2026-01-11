# https://leetcode.com/problems/min-cost-climbing-stairs/description
"""
Solution 1: DP with tabulation
TC: O(n)
SC: O(1)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2: return min(cost)
        cost.append(0) # cost at the top most step
        first, second = cost[0], cost[1]
        for i in range(2, n+1):
            nxt = min(first, second) + cost[i]
            first = second
            second = nxt
        return second