"""This is a Ghost object that travels from node to node"""
import pygame
from vectors import Vector2D
from pygame.locals import *
from ghostmovement import FourWayGhost
from constants import *
from levelnodes import Level1Nodes

class Ghost(object):
    def __init__(self, nodes, nodeVal):
        self.dim = ENTITYSIZE
        self.COLOR = BLUE
        self.speed = SPEED
        self.goal = Vector2D(10*TILEWIDTH,15*TILEHEIGHT)
        self.mode = SCATTER
        self.position = nodes[nodeVal].position
        self.mover = FourWayGhost(nodes, nodeVal, self)
        
    def checkModeChange(self, modeObj):
        if modeObj.modeChange:
            self.mode = modeObj.mode
            
    def update(self, dt):
        self.mover.update(dt)

    def attack(self):
        pass
    
    def scatter(self):
        self.goal = self.scatterGoal

    def setGoal(self, pacman):
        if self.mode == ATTACK:
            self.speed = SPEED
            self.attack(pacman)
        elif self.mode == SCATTER:
            self.speed = SPEED
            self.scatter()
        elif self.mode == FREIGHT:
            self.speed = FREIGHTSPEED
            
    def render(self, screen):
        x, y = self.position.toTuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), 8)
        #screen.blit(self.frameset[self.iframe], (x-16, y-16))

class Blinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, HOMEBASENODE)
        self.COLOR = RED
        self.scatterGoal = BLINKYGOAL
        
    def attack(self, pacman):
        self.goal = pacman.position


class Pinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, PINKYHOMENODE)
        self.COLOR = PINK
        self.scatterGoal = PINKYGOAL

    def attack(self, pacman):
        self.goal = pacman.position+DIRECTIONS[pacman.direction]*TILES4

class Inky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, INKYHOMENODE)
        self.COLOR = BLUE
        self.scatterGoal = INKYGOAL
        
    def setGoal(self, pacman, blinky):
        if self.mode == ATTACK:
            self.speed = SPEED
            self.attack(pacman, blinky)
        elif self.mode == SCATTER:
            self.speed = SPEED
            self.scatter()
        elif self.mode == FREIGHT:
            self.speed = FREIGHTSPEED
            
    def attack(self, pacman, blinky):
        self.goal = DIRECTIONS[pacman.direction]*TILES4 + pacman.position*2 \
                    - blinky.position

class Clyde(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, CLYDEHOMENODE)
        self.COLOR = TEAL
        self.scatterGoal = CLYDEGOAL
        
    def attack(self, pacman):
        pDiff = self.position - pacman.position
        if pDiff.magnitudeSquared() >= TILES8SQ:
            self.goal = pacman.position
        else:
            self.goal = CLYDEGOAL

