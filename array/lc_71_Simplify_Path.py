# https://leetcode.com/problems/simplify-path/
'''
Solution 1: Using stack
Runtime 23 ms Beats 99.98%
Memory 16.3 MB Beats 91.45%
TC:O(n)
SC:O(n)
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path)==1:return path
        can_path = []
        for e in path.split('/'):
            if e == '..':
                if can_path:
                    can_path.pop()
            elif e in {'', '.'}:
                continue
            else: can_path.append(e)
        result = '/'+'/'.join(can_path)
        del can_path
        return result