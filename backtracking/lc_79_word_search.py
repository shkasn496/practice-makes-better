# https://leetcode.com/problems/word-search/description/
"""
Solution : Backtracking

Runtime 5891 ms Beats 75.77%
Memory 16.5 MB Beats 23.19%

TC: O( (m*n)⋅3^L ) where (m*n) is the number of cells in the board and L is the 
length of the word to be matched. For the backtracking function, initially 
we could have at most 4 directions to explore, but further the 
choices are reduced into 3 (since we won't go back to where we come from). 
As a result, the execution trace after the first step could be visualized 
as a 3-ary tree, each of the branches represent a potential exploration in 
the corresponding direction. 
Therefore, in the worst case, the total number of invocation would be the 
number of nodes in a full 3-nary tree, which is about 3^L.

We iterate through the board for backtracking, i.e. there could be N times 
invocation for the backtracking function in the worst case.
SC:O(L) recursive stack space
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        N = len(word)
        if N > m*n:return False
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def backtrack(r, c, idx):
            # 1. Goal, Constraints
            if idx==N:return True
            # 2. Choices
            curr_elem = board[r][c]
            board[r][c]='#'#visiting curr word neighbors
            found_word=False
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n or \
                board[nr][nc]!=word[idx]:continue
                found_word=backtrack(nr, nc, idx+1)
                if found_word:break
            board[r][c]=curr_elem #board_elem = word[idx]
            return found_word
        word_found=False
        for r in range(m):
            for c in range(n):
                if board[r][c]!=word[0]:continue
                if backtrack(r,c,1):
                    word_found=True
                    break
            if word_found:break
        del directions
        return word_found