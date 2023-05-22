# https://leetcode.com/problems/flip-game/description/
"""
Solution: Just need to traverse between i--i+2
Runtime 37 ms Beats 50.46% 
Memory 16.6 MB Beats 27.78%
TC:O(n)
SC:O(n)
"""
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        output=[]
        for i in range(len(currentState)-1):
            c1, c2 = currentState[i],currentState[i+1]
            if c1==c2=='+':output.append(currentState[:i]+"--"+currentState[i+2:])
        return output