"""This is a Ghost object that travels from node to node"""
import pygame
from vectors import Vector2D
from pygame.locals import *
from ghostmovement import FourWayGhost
from constants import *
from collision import circleCircle as collided
from modeswitcher import ModeSwitcher

class Ghost(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.COLOR = BLUE
        self.speed = SPEED
        self.goal = Vector2D()
        self.modeUpdater = ModeSwitcher()
        self.reset()
        self.fleeGoal = self.move.nodes[self.nodes.base].position
        self.radius = 8
        self.released = False
        self.counter = 0

    def reset(self):
        '''Reset ghost to initial conditions'''
        self.nodes.reset()
        self.direction = LEFT
        self.position = self.nodes.resetHomePosition()
        self.move = FourWayGhost(self.nodes, self.nodes.home, self)
        self.speed = SPEED
        self.alive = True
        self.released = False
        self.counter = 0
        self.modeUpdater.reset()

    def checkModeChange(self):
        '''Change the ghosts mode if ghost is not in FLEE mode'''
        if self.modeUpdater.modeChange:
            if not self.modeUpdater.inFleeMode():
                #reverse direction
                if self.released:
                    self.move.reverseDirection()
            
    def update(self, dt):
        self.speed = self.modeUpdater.mode.speed
        self.move.update(dt)
        
    def attack(self, pacman=None, blinky=None):
        pass
    
    def scatter(self):
        self.goal = self.scatterGoal
        
    def freight(self):
        pass
        
    def flee(self):
        '''Send ghost home after being eaten'''
        self.goal = self.fleeGoal
        if self.reachedGoal(self.nodes.base):
            self.modeUpdater.setMode(self.modeUpdater.mode.setNextMode())
            self.releaseFromHome()

    def reachedGoal(self, nodeVal):
        '''Check if current node is the same as nodeVal'''
        if self.move.node == nodeVal:
            return True
        return False
        
    def setGoal(self, pacman, blinky=None):
        '''Set the goal based on the mode'''
        self.modeUpdater.mode.setGoal(self, pacman, blinky)
        
    def checkPacmanCollide(self, pacman):
        '''Check for collision between Pacman and ghost'''
        if collided(self, pacman):
            if not self.modeUpdater.inFleeMode():
                if self.modeUpdater.inFreightMode():
                    self.modeUpdater.overideMode()
                    self.sendHome()
                else:
                    pacman.alive = False
            
    def sendHome(self):
        self.nodes.sendHome()

    def releaseFromHome(self):
        self.nodes.releaseFromHome()


    def render(self, screen):
        x, y = self.position.toTuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), 8)
        #screen.blit(self.frameset[self.iframe], (x-16, y-16))

        
#==============================================================================
# INSTANCES OF THE GHOST CLASS:  BLINKY, PINKY, INKY, CLYDE
#==============================================================================
class Blinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = RED
        self.scatterGoal = BLINKYGOAL
        self.valueForRelease = 0
        
    def attack(self, pacman, blinky=None):
        self.goal = pacman.position
        
#==============================================================================
class Pinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = PINK
        self.scatterGoal = PINKYGOAL
        self.valueForRelease = 0
        
    def attack(self, pacman, blinky=None):
        self.goal = pacman.position+DIRECTIONS[pacman.direction]*TILES4
        
#==============================================================================
class Inky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = BLUE
        self.scatterGoal = INKYGOAL
        self.valueForRelease = 30
        
    #def setGoal(self, pacman, blinky):
    #    '''Set the goal based on the mode'''
    #    if self.mode == ATTACK:
    #        self.speed = SPEED
    #        self.attack(pacman, blinky)
    #    elif self.mode == SCATTER:
    #        self.speed = SPEED
    ##        self.scatter()
    # #   elif self.mode == FREIGHT:
    #        self.speed = FREIGHTSPEED
    #    elif self.mode == FLEE:
    #        self.speed = FLEESPEED
    #        self.flee()
        #elif self.mode == START:
        #    self.onStart()
            
    def attack(self, pacman, blinky=None):
        self.goal = DIRECTIONS[pacman.direction]*TILES4 + pacman.position*2 \
                    - blinky.position


#==============================================================================
class Clyde(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = TEAL
        self.scatterGoal = CLYDEGOAL
        self.valueForRelease = 60
        
    def attack(self, pacman, blinky=None):
        pDiff = self.position - pacman.position
        if pDiff.magnitudeSquared() >= TILES8SQ:
            self.goal = pacman.position
        else:
            self.goal = CLYDEGOAL
            

