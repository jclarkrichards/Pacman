
"""Creates the four ghost objects and handles them as a whole"""
from constants import *
from ghost import *
from levelnodes import *

class GhostGroup(object):
    def __init__(self):
        blinky, pinky, inky, clyde = self.createNodes()
        inky.additionalNodes()
        clyde.additionalNodes()
        self.blinky = Blinky(blinky)
        self.pinky = Pinky(pinky)
        self.inky = Inky(inky)
        self.clyde = Clyde(clyde)
        self.members = [self.blinky, self.pinky, self.inky, self.clyde]

    def createNodes(self):
        nodelist = []
        nodelist.append(Level1NodesBlinky())
        nodelist.append(Level1NodesPinky())
        nodelist.append(Level1NodesInky())
        nodelist.append(Level1NodesClyde())
        for nodes in nodelist:
            nodes.removeNodeLinks()
            nodes.setHomeNodes()
        return nodelist
    
    def update(self, dt):
        for ghost in self.members:
            ghost.update(dt)

    def checkModeChange(self, gameMode):
        for ghost in self.members:
            ghost.checkModeChange(gameMode)
        
    def checkPacmanCollide(self, pacman):
        for ghost in self.members:
            ghost.checkPacmanCollide(pacman)

    def setGoal(self, pacman):
        self.blinky.setGoal(pacman)
        self.pinky.setGoal(pacman)
        self.inky.setGoal(pacman, self.blinky)
        self.clyde.setGoal(pacman)

    def reverseDirection(self):
        for ghost in self.members:
            ghost.move.reverseDirection()
            
    def reset(self):
        for ghost in self.members:
            ghost.reset()
            
    def render(self, screen):
        '''Draw all of the ghosts'''
        for ghost in self.members:
            ghost.render(screen)

