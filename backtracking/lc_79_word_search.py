# https://leetcode.com/problems/word-search/description/
"""
Solution : Backtracking

Runtime 8303 ms Beats 34.95%
Memory 13.9 MB Beats 91.58%

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
        m,n = len(board),len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def backtrack(r,c,i):
            # conditions
            if not 0<=r<m or not 0<=c<n or i>=len(word) or\
            board[r][c]!=word[i] or board[r][c]=='#':return False
            #goal
            if i==len(word)-1 and board[r][c]==word[i]:return True
            board[r][c]="#"
            state=False
            #choices
            for dr,dc in directions:
                state=backtrack(r+dr,c+dc,i+1)
                if state:break
            board[r][c]=word[i]
            return state
        for r in range(m):
            for c in range(n):
                if backtrack(r,c,0): return True
        return False