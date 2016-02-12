"""position is a Vector2D"""
import pygame
from constants import *
from numpy import loadtxt
from collision import circleCircle as collided

class Pellet(object):
    def __init__(self, position):
        self.position = position
        self.radius = 3
        self.alive = True
        self.type = not POWERPELLET
        
    def render(self, screen):
        x, y = self.position.toTuple()
        pygame.draw.circle(screen, YELLOW, (int(x), int(y)), self.radius)
        
    
class PowerPellet(Pellet):
    def __init__(self, position):
        Pellet.__init__(self, position)
        self.radius = 8
        self.type = POWERPELLET

        
class PelletGroup(object):
    def __init__(self, pelletFile):
        self.file = pelletFile
        self.pelletList = []
        self.numEaten = 0
        self.numMax = 0
        
    def setupPellets(self):
        '''Input a file that indicates the location of the pellets'''
        layout = loadtxt(self.file, dtype=str)
        rows, cols = layout.shape
        for row in range(rows):
            for col in range(cols):
                position = Vector2D(TILEWIDTH*(col), TILEHEIGHT*(row))
                if layout[row][col] == 'p':
                    self.pelletList.append(Pellet(position))
                elif layout[row][col] == 'P':
                    self.pelletList.append(PowerPellet(position))
        self.numMax = len(self.pelletList)
        
    def update(self, pacman, gameMode):
        pList = [p for p in self.pelletList if p.alive]
        for pellet in pList:
            if collided(pacman, pellet):
                self.numEaten += 1
                pellet.alive = False
                if pellet.type == POWERPELLET:
                    gameMode.setMode(FREIGHT)
                break
                    
    def render(self, screen):
        for pellet in self.pelletList:
            if pellet.alive:
                pellet.render(screen)

