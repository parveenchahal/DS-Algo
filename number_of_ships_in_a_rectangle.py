# https://leetcode.com/problems/number-of-ships-in-a-rectangle/


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y or not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        mid_x, mid_y = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
        
        b1_tr = Point(mid_x, topRight.y)
        b1_bl = Point(bottomLeft.x, mid_y + 1)
        
        b2_tr = topRight
        b2_bl = Point(mid_x + 1, mid_y + 1)
        
        b3_tr = Point(topRight.x, mid_y)
        b3_bl = Point(mid_x + 1, bottomLeft.y)
        
        b4_tr = Point(mid_x, mid_y)
        b4_bl = bottomLeft
        
        count = 0
        count += self.countShips(sea, b1_tr, b1_bl)
        count += self.countShips(sea, b2_tr, b2_bl)
        count += self.countShips(sea, b3_tr, b3_bl)
        count += self.countShips(sea, b4_tr, b4_bl)
        
        return r
