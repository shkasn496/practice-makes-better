# https://leetcode.com/problems/number-of-ships-in-a-rectangle/description
"""
Brute force is s * O(m*n)
"""

"""
Solution 1: Binary Search / Divide n Conquer
TC: O(S * (log(max(M, N)) - log(S)))
SC: S * (log(max(M, N)))
"""

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y
        
        # 1. Border cases
        if x1 > x2 or y1 > y2: return 0
        
        # 2. if no ship
        if not sea.hasShips(topRight, bottomLeft): return 0

        # 3. if its a single point
        if (x1, y1) == (x2, y2):
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        
        # 4. divide into quadrants
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2

        total_ships = 0
        total_ships += self.countShips(sea, topRight, Point(mid_x+1, mid_y+1)) # top right exclude mid point
        total_ships += self.countShips(sea, Point(mid_x, y2), Point(x1, mid_y+1)) # top left exclude mid point
        total_ships += self.countShips(sea, Point(x2, mid_y), Point(mid_x+1, y1)) # bottom right exclude mid point
        total_ships += self.countShips(sea, Point(mid_x, mid_y), bottomLeft) # bottom left include mid point
        return total_ships