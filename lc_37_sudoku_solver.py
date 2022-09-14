#https://leetcode.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def conditions(r, c, n):
            # check all elements/columns in row / check all elements/rows in column
            for i in range(9):
                if board[r][i] == str(n) or board[i][c] ==str(n): return False
            # check sub-grid, get the sub grid start point
            sub_r, sub_c = (r // 3)*3, (c//3)*3
            for i in range(sub_r, sub_r+3):
                for j in range(sub_c, sub_c+3):
                    if board[i][j]==str(n):return False
            return True
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c]!=".":continue
                    for n in range(1,10):
                        if conditions(r, c, n):
                            board[r][c]=str(n)
                            if solve():return True
                            board[r][c]="."#backtrack if solution didnt work
                    return False
            return True
        return solve()