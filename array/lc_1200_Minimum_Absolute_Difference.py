# https://leetcode.com/problems/minimum-absolute-difference/description

"""
TC: O(nlogn)
SC:O(1)
"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) < 2: return []
        arr.sort()
        result = [[arr[0], arr[1]]]
        for num1, num2 in zip(arr[1:], arr[2:]):
            dist = abs(num2 - num1)
            while result and abs(result[-1][1] - result[-1][0]) > dist:
                result.pop()
            if not result or abs(result[-1][1] - result[-1][0]) == dist:
                result.append([num1, num2])
        return result