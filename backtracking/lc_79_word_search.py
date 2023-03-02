# https://leetcode.com/problems/word-search/description/
"""
Solution : Backtracking

Runtime 7213 ms Beats 59.45%
Memory 13.8 MB Beats 90.75%

TC: O(N⋅3^L ) where N is the number of cells in the board and L is the length of the word to be matched
For the backtracking function, initially we could have at most 4 directions to explore, but further the 
choices are reduced into 3 (since we won't go back to where we come from). As a result, the execution 
trace after the first step could be visualized as a 3-ary tree, each of the branches represent a 
potential exploration in the corresponding direction. 
Therefore, in the worst case, the total number of invocation would be the number of nodes in a 
full 3-nary tree, which is about 3^L.

We iterate through the board for backtracking, i.e. there could be N times invocation for 
the backtracking function in the worst case.
SC:O(L) recursive stack space
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        if len(word)>m*n:return False
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def backtrack(r, c, idx):
            # Goal
            if idx>=len(word):return True
            #1. Conditions
            if not 0<=r<m or not 0<=c<n or \
            board[r][c]!=word[idx]:return False
            #3. Choices
            board[r][c]='#'#visited
            for dr,dc in directions:
                if backtrack(r+dr, c+dc, idx+1):return True
            board[r][c]=word[idx]#backtrack
            return False
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):return True
        del directions
        return False