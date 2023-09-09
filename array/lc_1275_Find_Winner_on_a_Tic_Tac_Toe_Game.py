# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
"""
Solution 1: Create a board that maintains the board states. 
            Check the board rows, cols, diagonal and anti-diagonal to find winner.

Runtime 27 ms Beats 99.13%
Memory 16.2 MB Beats 96.30%

TC: O(m * n) where m = len(moves) and n=grid size
SC: O(n^2) because of 2d grid
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        pending_moves = 9
        n = 3
        # A = 1, B = 2
        board = [[0]*n for _ in range(n)]
        # Check if any of 4 winning conditions to see if the current player has won.
        def checkRow(row, player_id):
            for col in range(n):
                if board[row][col] != player_id:
                    return False
            return True

        def checkCol(col, player_id):
            for row in range(n):
                if board[row][col] != player_id:
                    return False
            return True

        def checkDiagonal(player_id):
            for row in range(n):
                if board[row][row] != player_id:
                    return False
            return True

        def checkAntiDiagonal(player_id):
            for row in range(n):
                if board[row][n - 1 - row] != player_id:
                    return False
            return True

        def check_board_state(row, col, player):
            if checkRow(row, player) or checkCol(col, player) or \
            (row == col and checkDiagonal(player)) or \
            (row + col == n - 1 and checkAntiDiagonal(player)):
                return player
            return 0

        for i, (r,c) in enumerate(moves):
            pending_moves -= 1
            player = 1 if i%2 == 0 else 2
            board[r][c] = player
            state = check_board_state(r, c, player)
            if state==player:
                return "A" if player == 1 else "B"
        del board
        return "Draw" if not pending_moves else "Pending"

"""
Solution 2: Optimized time and memory solution.
            Store one array for rows, one array for cols, and two variables
            for diagonal and anti_diagonal.
            Player A = 1 and Player B = -1

Runtime 27 ms Beats 99.13%
Memory 16.3 MB Beats 50.28%

TC: O(m) the update_board_state() and check_board_state() take constant time
SC: O(n) array for rows and cols
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        player_A, player_B = 1, -1
        pending_moves = n * n
        rows, cols, diag, anti_diag = [0]*n, [0]*n, 0, 0
        
        def update_board_state(r, c, player):
            nonlocal diag, anti_diag
            rows[r] += player
            cols[c] += player
            if r==c: diag += player
            if r+c == n-1 : anti_diag += player
            return

        def check_board_state(row, col):
            nonlocal diag, anti_diag
            if abs(diag) == n:return player_A if diag > 0 else player_B
            if abs(anti_diag) == n:return player_A if anti_diag > 0 else player_B

            for idx in range(n):
                if abs(rows[idx]) == n:return player_A if rows[idx]>0 else player_B
                elif abs(cols[idx]) == n:return player_A if cols[idx]>0 else player_B

            return 0

        for i, (r,c) in enumerate(moves):
            pending_moves -= 1
            player = player_A if i%2 == 0 else player_B
            update_board_state(r, c, player)
            state = check_board_state(r, c)
            if state==player:
                return "A" if player == player_A else "B"
        del rows, cols 
        return "Draw" if not pending_moves else "Pending"