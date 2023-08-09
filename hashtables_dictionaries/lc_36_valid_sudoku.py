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

"""
Solution 2: (Fastest solution) Use a set to store the row and val, val and col, and sub_box and val.
            Check if this val is present in the existing set.
Runtime 85 ms Beats 99.85%
Memory 16.4 MB Beats 53.47%

TC:O(n^2)
SC:O(n^2)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val =='.':continue
                if (r, val) in result or (val, c) in result or \
                (r//3, c//3, val) in result:
                    del result
                    return False
                result.add((r, val))
                result.add((val, c))
                result.add((r//3, c//3, val))
        del result
        return True

"""
Solution 3: Slower solution as it passes through the board row, col and subbox
            But doesn't use any additional memory
Runtime 97 ms Beats 96.7%
Memory 16.2 MB Beats 81.67%

TC:O(n^2) * (O(n)) = O(n^3)
            - O(n^2) for traversing the board. O(n) inside each r,c for satisfying the rules
SC:O(1)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        def can_satisfy_rules(r,c, val):
            for i in range(n):
                if i==r or i==c:continue
                if board[r][i]==val or board[i][c]==val:
                    return False
            subbox_r, subbox_c = (r//3)*3, (c//3)*3
            for ri in range(subbox_r, subbox_r+3):
                for ci in range(subbox_c, subbox_c+3):
                    if (ri, ci)==(r,c):continue
                    if board[ri][ci]==val:
                        return False
            return True
        for r in range(n):
            for c in range(n):
                if board[r][c]=='.':
                    continue
                if not can_satisfy_rules(r,c, board[r][c]):
                    return False
        return True