# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""
Solution 1: Backtracking
Runtime 22 ms Beats 98.84%
Memory 14 MB Beats 23.21%
TC: O((4^N)*N) where N is len(digits) and 4 is max number of chars attached to a digit.
SC: O(N) for recursive stack . Not taking into account the space taken by output
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<1:return []
        mapping = {'2':['a','b','c'],
                  '3':['d','e','f'],
                  '4':['g','h','i'],
                  '5':['j','k','l'],
                  '6':['m', 'n','o'],
                  '7':['p','q','r','s'],
                  '8':['t','u','v'],
                  '9':['w','x','y','z']}
        combinations=set()
        N = len(digits)
        def backtrack(idx, subarray):
            # 1. conditions
            if idx>N:return
            # 2. goal
            if idx==N:
                if len(subarray)!=N:return
                comb="".join(subarray)
                if comb not in combinations:
                    combinations.add(comb)
                del comb
                return
            # 3. choices
            for c in mapping[digits[idx]]:
                backtrack(idx+1,subarray+[c])
        backtrack(0,[])
        del mapping
        return combinations