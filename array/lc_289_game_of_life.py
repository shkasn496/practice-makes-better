# https://leetcode.com/problems/game-of-life/description/
"""
Solution 1: Using mxn space to store neighbor info
Runtime 30 ms Beats 88.6%
Memory 13.9 MB Beats 84.43%
TC:O(m*n)
SC:O(m*n)
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        m, n = len(board), len(board[0])
        # calculate neighbors of current board state
        neighbors = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if not 0<=nr<m or not 0<=nc<n:continue
                    if board[nr][nc]:neighbors[r][c]+=1
        # update board state based on rules
        for r in range(m):
            for c in range(n):
                if board[r][c]:
                    if neighbors[r][c]<2 or neighbors[r][c]>3:
                        board[r][c]=0
                else:
                    if neighbors[r][c]==3:
                        board[r][c]=1
        del neighbors, directions
        return

"""
Solution 2 : Followup question: Space optimization using no extra memory
        # update board state based on rules
        # live cell dies denoted as -1
        # dead cell alive denoted as 2
Runtime 28 ms Beats 92.6%
Memory 13.9 MB Beats 84.43%
TC:O(m*n)
SC:O(1)
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        m, n = len(board), len(board[0])    
        # update board state based on rules
        # live cell dies denoted as -1
        # dead cell alive denoted as 2
        def calculate_neighbors(r,c):
            neighbors=0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n:continue
                if abs(board[nr][nc])==1:neighbors+=1
            return neighbors

        for r in range(m):
            for c in range(n):
                neighbors = calculate_neighbors(r,c)
                if board[r][c]: #alive cell
                    if neighbors<2 or neighbors>3:
                        board[r][c]=-1
                else: # dead cell
                    if neighbors==3:
                        board[r][c]=2
        # reset the state changes
        for r in range(m):
            for c in range(n):
                if board[r][c]==-1:board[r][c]=0
                elif board[r][c]==2:board[r][c]=1
        del directions
        return