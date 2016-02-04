
"""Creates the four ghost objects and handles them as a whole"""
from constants import *
from ghost import *

class GhostGroup(object):
    def __init__(self):
        blinkyNodes = self.setNodes()
        pinkyNodes = self.setNodes()
        inkyNodes = self.setNodes()
        clydeNodes = self.setNodes()
        inkyNodes.setInkyNodes()
        clydeNodes.setClydeNodes()
        self.blinky = Blinky(blinkyNodes)
        self.pinky = Pinky(pinkyNodes)
        self.inky = Inky(inkyNodes)
        self.clyde = Clyde(clydeNodes)

    def update(self, dt):
        self.blinky.update(dt)
        self.pinky.update(dt)
        self.inky.update(dt)
        self.clyde.update(dt)

    def checkModeChange(self, gameMode):
        self.blinky.checkModeChange(gameMode)
        self.pinky.checkModeChange(gameMode)
        self.inky.checkModeChange(gameMode)
        self.clyde.checkModeChange(gameMode)

    def setGoal(self, pacman):
        self.blinky.setGoal(pacman)
        self.pinky.setGoal(pacman)
        self.inky.setGoal(pacman, self.blinky)
        self.clyde.setGoal(pacman)

    def setNodes(self):
        nodes = Level1Nodes()
        nodes.adjustGhostNodes()
        nodes.setHomeNodes()
        return nodes
    
    def render(self, screen):
        self.blinky.render(screen)
        self.pinky.render(screen)
        self.inky.render(screen)
        self.clyde.render(screen)
