# https://leetcode.com/problems/product-of-the-last-k-numbers/description/
"""
Solution:
Runtime 261 ms Beats 99.14%
Memory 28.7 MB Beats 79.64%

TC: O(1)
SC: O(n)
"""
class ProductOfNumbers:

    def __init__(self):
        self.products=[1]
        return

    def add(self, num: int) -> None:
        if num: self.products.append(self.products[-1]*num)
        else: self.__init__()
        return
        
    def getProduct(self, k: int) -> int:
        if len(self.products)<=k :return 0
        return self.products[-1] // self.products[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)