# https://leetcode.com/problems/valid-word-square/description/
"""
Solution: Compare row and col
Runtime 63 ms Beats 79.1%
Memory 17.2 MB Beats 14.51%
TC:O(m*n)
SC:O(1)
"""
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows, cols = len(words), len(words[0])
        if rows!=cols:return False
        r, c = 0,0
        while r<rows and c<cols:
            word1 = words[r]
            word2 = "".join([word[c] for word in words if c<len(word)])
            if word1!=word2:return False
            r+=1
            c+=1
        return True