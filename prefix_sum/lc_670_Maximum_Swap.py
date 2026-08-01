# https://leetcode.com/problems/maximum-swap/description
"""
TC: O(N)
SC:O(n)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_arr = []
        while num:
            digit = num % 10
            num //= 10
            num_arr.append(digit)
        num_arr = num_arr[::-1]
        n = len(num_arr)
        for i in range(n-1, -1, -1):
            if i == n-1:
                num_arr[i] = [num_arr[i], num_arr[i], i]
            else:
                prev_num, prev_max, prev_idx = num_arr[i+1]
                if num_arr[i] > prev_max:
                    num_arr[i] = [num_arr[i], num_arr[i], i]
                else:
                    num_arr[i] = [num_arr[i], prev_max, prev_idx]
        for curr_idx, (curr_num, curr_max, max_idx) in enumerate(num_arr):
            if curr_num < curr_max:
                num_arr[curr_idx], num_arr[max_idx] = num_arr[max_idx], \
                num_arr[curr_idx]
                break
        num = 0
        for elem in num_arr:
            n, _, _ = elem
            num = num * 10 + n
        del num_arr
        return num