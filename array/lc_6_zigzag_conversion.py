# https://leetcode.com/problems/zigzag-conversion/description/?envType=company&envId=facebook&favoriteSlug=facebook-all
"""
Solution :
TC: O(n)
SC: O(n)
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or n == numRows : return s
        cache = [''] * numRows
        row = 0
        direction = 1 # 1-> down, -1 -> up
        for c in s:
            cache[row] += c
            if row == 0:
                direction = 1
            else:
                direction = -1
            row += direction
        return "".join(cache)