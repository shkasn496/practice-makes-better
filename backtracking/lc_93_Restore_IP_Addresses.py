# https://leetcode.com/problems/restore-ip-addresses/description/
"""
TC: O(M^N * N) where M can be max upto 3, and N = 4 to indicate how many integers in total
SC: O(1)
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4: return []
        result = []
        def backtrack(start_idx, ans):
            if len(ans) >= 4 and start_idx < len(s):
                return
            if len(ans) == 4 and start_idx == len(s):
                result.append(".".join(ans))
                return
            for size in range(1, 4):
                end_idx = start_idx + size
                if end_idx > len(s): continue
                substr = s[start_idx: end_idx]
                if len(substr) > 3 or (len(substr) > 1 and substr[0] == '0'):
                    continue
                if int(substr) <= 255:
                    backtrack(end_idx, ans + [substr])
            return
        backtrack(0, [])
        return result