# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
"""
Solution 1: Keep track of min_price and max_profit
Runtime 748 ms Beats 99.92%
Memory 27.4 MB Beats 58%
TC:O(n)
SC:O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price: min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit