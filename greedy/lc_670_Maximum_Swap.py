# https://leetcode.com/problems/maximum-swap/description/
"""
Solution 1: Greedy solution.
            First, create a dictionary with digit of nums as keys and their latest indexes as values.
            Then, iterate over the nums array from left to right. 
                If I come across a digit < 9, then go over the range(9, digit+1) to check if its
                present in the dictionary and if its latest index is after curr_idx.
                If yes, swap the elements and return the num.

Runtime 24 ms Beats 99.84%
Memory 16.2 MB Beats 71.31%
TC:O(n)
SC:O(n)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:return num
        num = list(str(num))
        # dictionary with key=digit, value = latest index
        digit_occ = {n: i for i, n in enumerate(num)}
        # iterate over num array from left to right
        for curr_idx, n in enumerate(num):
            if n=='9':continue
            for digit in range(9, int(n), -1):
                if str(digit) not in digit_occ:continue
                latest_idx = digit_occ[str(digit)]
                if latest_idx <= curr_idx:continue
                # perform swap
                num[curr_idx], num[latest_idx] = num[latest_idx], num[curr_idx]
                del digit_occ
                return int("".join(num))
        del digit_occ
        return int("".join(num))