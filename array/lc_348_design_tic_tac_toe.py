# https://leetcode.com/problems/design-tic-tac-toe/description/
"""
Solution 1: Create a 2d array and iterate through row col 
Runtime 85 ms Beats 89.91%
Memory 17 MB Beats 7.37%
init():
    TC: O(n)
    SC: O(n^2)

move():
    TC: O(1) + search()
    SC: O(1)

_search():
    TC: 4* O(n)
    SC: O(1)
"""
class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for i in range(n)]
        self.n = n
        return

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col]=player
        return self._search(row, col, player)

    def _search(self, row: int, col: int, player: int) -> int:
        for i in range(self.n):# all cols of row
            if i==self.n - 1 and self.board[row][i]== player:return player
            if self.board[row][i]!= player:
                break
        for i in range(self.n):#all rows of column
            if i==self.n - 1 and self.board[i][col]== player:return player
            if self.board[i][col]!= player:
                break
        if row == col: #right diagonal
            for i in range(self.n):
                if i==self.n - 1 and self.board[i][i]== player:return player
                if self.board[i][i]!= player:
                    break
        if row + col == self.n - 1:# check inverse diagonal
            for i in range(self.n):
                    if i==self.n - 1 and self.board[i][self.n-i-1]== player:return player
                    if self.board[i][self.n-i-1]!= player:
                        break
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)