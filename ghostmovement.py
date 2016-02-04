import pygame
from pygame.locals import *
from vectors import Vector2D
from nodemovement3 import *
from constants import *
from random import randint

class FourWayGhost(FourWayContinuous):
    def __init__(self, node, entity):
        '''node is the starting node.  All other nodes are connected
        entity is the entity that travels from node to node'''
        FourWayContinuous.__init__(self, node, entity)
        self.chooseDirection()
        self.setEntityDirection(self.direction)
        
    def update(self, dt):
        self.moveTowardsTarget(dt)
        
        if self.overshotTarget():
            self.node = self.target
            self.removeOppositeDirection()
            self.portal()

            if self.entity.mode == FREIGHT:
                self.chooseRandomDirection()
            else:
                self.chooseDirection()

            if self.direction != self.entity.direction:
                self.entity.position = self.node.position
                self.setEntityDirection(self.direction)
            else:
                self.setTarget(self.entity.direction)
        
    def keyDiscrete(self, key):
        pass
    
    def keyContinuous(self, key):
        pass
    
    def chooseDirection(self):
        if len(self.validDirections) > 1:
            d = []
            for direction in self.validDirections:
                checkPos = self.entity.position + DIRECTIONS[direction]*TILEWIDTH
                checkPos -= self.entity.goal
                d.append(checkPos.magnitudeSquared())
            i = d.index(min(d))
            self.direction = self.validDirections[i]
        else:
            self.direction = self.validDirections[0]

    def chooseRandomDirection(self):
        if len(self.validDirections) > 1:
            i = randint(0, len(self.validDirections)-1)
            self.direction = self.validDirections[i]
        else:
            self.direction = self.validDirections[0]

