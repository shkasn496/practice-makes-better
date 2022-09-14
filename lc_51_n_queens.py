# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        result = []
        def constraints(r, c):
            for i in range(n):
                if board[r][i] == "Q" or board[i][c] == "Q":return False
            #right diagonal r+c = constant, left diagonal r-c = constant
            r_diag, l_diag=[], []
            for temp_r in range(n):
                right_c, left_c = (r+c) - temp_r, temp_r - (r-c)
                if 0<=right_c <n: r_diag.append((temp_r, right_c))
                if 0<=left_c <n: l_diag.append((temp_r, left_c))   
            for new_r, new_c in r_diag: 
                if board[new_r][new_c] == "Q":return False
            for new_r, new_c in l_diag: 
                if board[new_r][new_c] == "Q":return False
            del r_diag, l_diag
            return True          
        def dfs(r):
            if r==n:
                result.append(["".join(elem) for elem in board])
                return
            for c in range(n):
                if constraints(r, c):
                    board[r][c]="Q" #choice
                    dfs(r+1)
                    board[r][c]="." #backtracking      
            return
        dfs(0)
        del board
        return result 