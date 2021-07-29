# https://leetcode.com/problems/robot-room-cleaner/


class Solution:
    
    _directions = (
        (-1, 0), # Up
        (0, 1), # Right
        (1, 0), # Down
        (0, -1) # Left
    )
    
    def _go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
    # Directions 0: up, 1: right, 2: down, 3: left
    def _dfs(self, u, robot, visited, dir):
        i, j = u
        robot.clean()
        visited.add(u)
        
        for k in range(4):
            new_dir = (dir + k) % 4
            v = (i + self._directions[new_dir][0], j + self._directions[new_dir][1])
            if v not in visited and robot.move():
                self._dfs(v, robot, visited, new_dir)
                self._go_back(robot)
            robot.turnRight()
    
    def cleanRoom(self, robot):
        visited = set()
        self._dfs((0, 0), robot, visited, 0)

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
