# https://leetcode.com/problems/coin-change/description/
"""
Runtime 1430 ms Beats 93.22%
Memory 14.1 MB Beats 86.48%

TC: O(A*n) where A=amount and n=len(coins)
SC: O(A)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:return 0
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a]=min(dp[a], 1+dp[a-c])
        coinChanges=dp[amount]
        del dp
        return coinChanges if coinChanges< amount+1 else -1 