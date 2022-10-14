# https://leetcode.com/problems/counting-bits/
"""
Success
Details 
Runtime: 73 ms, faster than 99.35% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 78.94% of Python3 online submissions for Counting Bits.
TC: O(n)
SC: O(1)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n+1)]
        # bit_count() works the same as bin().count("1") but is 6x faster