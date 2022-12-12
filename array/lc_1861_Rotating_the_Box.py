# https://leetcode.com/problems/rotating-the-box/description/
"""
 Runtime 2399 ms Beats 95.6%
Memory 24.3 MB Beats 83.48%
TC: O(m*n)
SC: O(1) (not including result)
"""
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for r in range(m):
            empty = 0
            for c in reversed(range(n)):
                cell = box[r][c]
                if cell==".":
                    empty+=1
                elif cell=="*":
                    empty=0 # reset empty count
                else: # found a stone
                    if empty:
                        box[r][c+empty]=cell
                        box[r][c]="."
        return zip(*reversed(box)) #rotate the array #[list(reversed(i)) for i in zip(*box)]