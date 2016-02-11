"""This is a Ghost object that travels from node to node"""
import pygame
from vectors import Vector2D
from pygame.locals import *
from ghostmovement import FourWayGhost
from constants import *
from levelnodes import Level1Nodes
from collision import circleCircle as collided

class Ghost(object):
    def __init__(self, nodes, nodeVal):
        self.dim = ENTITYSIZE
        self.COLOR = BLUE
        self.speed = SPEED
        self.goal = Vector2D(10*TILEWIDTH,15*TILEHEIGHT)
        self.mode = SCATTER
        self.position = nodes.nodeDict[nodeVal].position
        self.move = FourWayGhost(nodes, nodeVal, self)
        self.nodeObj = nodes
        self.fleeGoal = self.move.nodes[HOMEBASENODE].position
        self.radius = 8
        
    def checkModeChange(self, modeObj):
        '''Change the ghosts mode if ghost is not in FLEE mode'''
        if modeObj.modeChange:
            if self.mode != FLEE:
                self.mode = modeObj.mode
            
    def update(self, dt):
        self.move.update(dt)

    def attack(self):
        pass
    
    def scatter(self):
        self.goal = self.scatterGoal
        
    def flee(self):
        '''Send ghost home after being eaten'''
        self.goal = self.fleeGoal
        if self.reachedGoal(HOMEBASENODE):
            self.mode = SCATTER
            self.releaseFromHome()

    def reachedGoal(self, nodeVal):
        '''Check if current node is the same as nodeVal'''
        if self.move.node == nodeVal:
            return True
        return False
        
    def setGoal(self, pacman):
        '''Set the goal based on the mode'''
        if self.mode == ATTACK:
            self.speed = SPEED
            self.attack(pacman)
        elif self.mode == SCATTER:
            self.speed = SPEED
            self.scatter()
        elif self.mode == FREIGHT:
            self.speed = FREIGHTSPEED
        elif self.mode == FLEE:
            self.speed = FLEESPEED
            self.flee()
            
    def checkPacmanCollide(self, pacman):
        if collided(self, pacman):
            if self.mode == FREIGHT:
                self.mode = FLEE
                self.sendHome()
            else:
                pacman.alive = False
            
    def sendHome(self):
        pass
            
    def render(self, screen):
        x, y = self.position.toTuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), 8)
        #screen.blit(self.frameset[self.iframe], (x-16, y-16))

#==============================================================================
# INSTANCES OF THE GHOST CLASS:  BLINKY, PINKY, INKY, CLYDE
#==============================================================================
class Blinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, HOMEBASENODE)
        self.COLOR = RED
        self.scatterGoal = BLINKYGOAL
        
    def attack(self, pacman):
        self.goal = pacman.position

#==============================================================================
class Pinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, PINKYHOMENODE)
        self.COLOR = PINK
        self.scatterGoal = PINKYGOAL

    def attack(self, pacman):
        self.goal = pacman.position+DIRECTIONS[pacman.direction]*TILES4

#==============================================================================
class Inky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes, INKYHOMENODE)
        self.COLOR = BLUE
        self.scatterGoal = INKYGOAL
        
    def setGoal(self, pacman, blinky):
        '''Set the goal based on the mode'''
        if self.mode == ATTACK:
            self.speed = SPEED
            self.attack(pacman, blinky)
        elif self.mode == SCATTER:
            self.speed = SPEED
            self.scatter()
        elif self.mode == FREIGHT:
            self.speed = FREIGHTSPEED
        elif self.mode == FLEE:
            self.speed = FLEESPEED
            self.flee()
            
    def attack(self, pacman, blinky):
        self.goal = DIRECTIONS[pacman.direction]*TILES4 + pacman.position*2 \
                    - blinky.position
                    
    def releaseFromHome(self):
        '''Release Inky from his home'''
        self.nodeObj.releaseInkyFromHome()
        
    def sendHome(self):
        self.nodeObj.sendInkyBackHome()

#==============================================================================
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
            
    def releaseFromHome(self):
        self.nodeObj.releaseClydeFromHome()
        
    def sendHome(self):
        self.nodeObj.sendClydeBackHome()

