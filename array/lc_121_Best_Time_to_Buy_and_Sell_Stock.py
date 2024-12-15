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
        if len(prices) < 2:return 0
        buy_price = prices[0]
        profit = 0
        for sell_price in prices[1:]:
            if sell_price < buy_price:
                buy_price = sell_price
            else:profit = max(profit, sell_price-buy_price)
        return profit