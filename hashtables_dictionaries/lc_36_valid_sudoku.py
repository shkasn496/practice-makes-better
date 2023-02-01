# https://leetcode.com/problems/valid-sudoku/description/
"""
Solution 1: Using a dictionary of sets
Runtime 90 ms Beats 94.73%
Memory 13.9 MB Beats 76.7%
TC:O(n^2)
SC:O(n^2)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        checks = collections.defaultdict(set)
        for r in range(m):
            for c in range(m):
                elem = board[r][c]
                if elem == '.':continue
                #check row
                if elem in checks[r]:return False
                checks[r].add(elem)
                #check col
                if elem in checks[c+9]:return False
                checks[c+9].add(elem)
                #check sub-box
                box_r, box_c = r//3, c//3
                if elem in checks[(box_r, box_c)]:return False
                checks[(box_r, box_c)].add(elem)
        del checks
        return True