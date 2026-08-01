# https://leetcode.com/problems/fruit-into-baskets/description/
"""
Solution 1: Sliding window
TC: O(n)
SC: O(2) hash map
"""
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        basket = defaultdict(int)
        i = 0
        for j in range(len(fruits)):
            basket[fruits[j]] += 1
            if len(basket) > 2:
                basket[fruits[i]] -= 1
                if basket[fruits[i]] == 0:
                    del basket[fruits[i]]
                i+=1
            max_fruits = max(max_fruits, j - i + 1)
        del basket
        return max_fruits