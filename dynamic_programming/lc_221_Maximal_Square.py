# https://leetcode.com/problems/maximal-square/description/
"""
Solution 1: DP with tabulation
TC: O(m*n)
SC: O(n)

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev_row = [int(matrix[0][c]) for c in range(n)]
        max_length = max(prev_row)
        for r in range(1, m):
            curr_row = [0] * n
            for c in range(n):
                if matrix[r][c] == '0': continue
                if c == 0: 
                    curr_row[c] = 1
                    continue
                # diag, top, left
                curr_row[c] = min(prev_row[c-1], prev_row[c], curr_row[c-1]) + 1
            prev_row = curr_row
            max_length = max(max(prev_row), max_length)
        del prev_row
        return max_length ** 2