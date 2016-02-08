import pygame
from pygame.locals import *
from vectors import Vector2D
from nodemovement import *

class FourWayContinuous(FourWayAbstract):
    def __init__(self, nodes, nodeVal, entity):
        '''node is the starting node.  All other nodes are connected
        entity is the entity that travels from node to node'''
        FourWayAbstract.__init__(self, nodes, nodeVal, entity)
        if self.entity.direction in self.validDirections:
            self.setEntityDirection(self.entity.direction)

    def update(self, dt):
        self.moveTowardsTarget(dt)
        
        if self.overshotTarget():
            self.node = self.target
            self.portal()
            #self.validDirections = self.node.neighbors.keys()
            self.setValidDirections()
            if self.direction in self.validDirections:
                if self.direction != self.entity.direction:
                    self.entity.position = self.nodes[self.node].position
                    self.setEntityDirection(self.direction)
                else:
                    self.setTarget(self.entity.direction)
            else:
                if self.entity.direction in self.validDirections:
                    self.setTarget(self.entity.direction)
                else:
                    self.entity.position = self.nodes[self.node].position
                    self.entity.direction = STOP
        else:
            if self.entity.direction == STOP:
                if self.direction in self.validDirections:
                    self.setEntityDirection(self.direction)
            else:
                if self.direction == self.entity.direction*-1:
                    self.reverseDirection()

    def keyDiscrete(self, key):
        pass
