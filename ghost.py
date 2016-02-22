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
        #self.direction = STOP
        self.goal = Vector2D()
        #self.mode = START
        self.reset()
        #self.move = FourWayGhost(nodes, self.nodes.home, self)
        self.fleeGoal = self.move.nodes[self.nodes.base].position
        self.radius = 8
        self.released = False
        self.modeUpdater = ModeSwitcher()

    def reset(self):
        '''Reset ghost to initial conditions'''
        self.nodes.reset()
        self.direction = STOP
        self.position = self.nodes.resetHomePosition()
        self.move = FourWayGhost(self.nodes, self.nodes.home, self)
        self.speed = SPEED
        self.mode = START
        self.alive = True
        self.released = False

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
        
    def freight(self):
        pass
        
    def flee(self):
        '''Send ghost home after being eaten'''
        self.goal = self.fleeGoal
        if self.reachedGoal(self.nodes.base):
            self.mode = SCATTER
            self.releaseFromHome()

    def reachedGoal(self, nodeVal):
        '''Check if current node is the same as nodeVal'''
        if self.move.node == nodeVal:
            return True
        return False
        
    def setGoal(self, pacman):
        '''Set the goal based on the mode'''
        self.modeUpdater.mode.setGoal(pacman, blinky)
        
        #if self.mode == ATTACK:
        #    self.speed = SPEED
        #    self.attack(pacman)
        #elif self.mode == SCATTER:
        #    self.speed = SPEED
        #    self.scatter()
        #elif self.mode == FREIGHT:
        #    self.speed = FREIGHTSPEED
        #elif self.mode == FLEE:
        #    self.speed = FLEESPEED
        #    self.flee()
        #elif self.mode == START:
        #    self.reset()

    def checkPacmanCollide(self, pacman):
        '''Check for collision between Pacman and self'''
        if collided(self, pacman):
            if self.mode != FLEE:
                if self.mode == FREIGHT:
                    self.mode = FLEE
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
        
    def attack(self, pacman):
        self.goal = pacman.position
        
#==============================================================================
class Pinky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = PINK
        self.scatterGoal = PINKYGOAL
        self.valueForRelease = 0
        
    def attack(self, pacman):
        self.goal = pacman.position+DIRECTIONS[pacman.direction]*TILES4
        
#==============================================================================
class Inky(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = BLUE
        self.scatterGoal = INKYGOAL
        self.valueForRelease = 40
        
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
            
    def attack(self, pacman, blinky):
        self.goal = DIRECTIONS[pacman.direction]*TILES4 + pacman.position*2 \
                    - blinky.position

    def resetMore(self):
        self.direction = UP
#==============================================================================
class Clyde(Ghost):
    def __init__(self, nodes):
        Ghost.__init__(self, nodes)
        self.COLOR = TEAL
        self.scatterGoal = CLYDEGOAL
        self.valueForRelease = 80
        
    def attack(self, pacman):
        pDiff = self.position - pacman.position
        if pDiff.magnitudeSquared() >= TILES8SQ:
            self.goal = pacman.position
        else:
            self.goal = CLYDEGOAL
            

