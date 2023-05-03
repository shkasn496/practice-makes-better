# https://leetcode.com/problems/minesweeper/description/
"""
Solution 1: Using DFS
Runtime 184 ms Beats 53.86%
Memory 19.2 MB Beats 5.40%
TC: O(M*N)
SC:O(M+N)
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        def dfs(r, c):
            neighbor_mine=0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n:continue
                if board[nr][nc]=='M':neighbor_mine+=1
            if neighbor_mine:board[r][c]=str(neighbor_mine)
            else:
                board[r][c]='B'
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not 0<=nr<m or not 0<=nc<n:continue
                    if board[nr][nc]=='E':dfs(nr,nc)
            return
        dfs(click[0],click[1])
        return board


"""
Cleaner reference code with comments, but same algorithm
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # check if clicked cell is a mine
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # define directions to search for mines
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # define a helper function to count adjacent mines
        def countMines(row, col):
            count = 0
            for r, c in dirs:
                if 0 <= row+r < len(board) and 0 <= col+c < len(board[0]) and board[row+r][col+c] == 'M':
                    count += 1
            return count

        # define a helper function for dfs to reveal empty cells
        def dfs(row, col):
            # check if current cell is out of bounds or already revealed
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != 'E':
                return

            # count adjacent mines and update current cell
            mines = countMines(row, col)
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for r, c in dirs:
                    dfs(row+r, col+c)

        # call dfs on clicked cell and return board
        dfs(click[0], click[1])
        return board