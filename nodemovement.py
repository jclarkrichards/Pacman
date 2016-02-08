import pygame
from pygame.locals import *
from vectors import Vector2D
from constants import *

class FourWayAbstract(object):
    def __init__(self, nodes, nodeVal, entity):
        '''node is the starting node.  All other nodes are connected
        entity is the entity that travels from node to node'''
        self.nodes = nodes
        self.node = nodeVal
        self.target = nodeVal
        self.entity = entity
        self.direction = STOP
        self.entity.direction = STOP
        self.validDirections = self.node.neighbors.keys()

    def update(self, dt):
        pass

    def setEntityDirection(self, direction):
        '''Set valid directions when in between nodes'''
        self.entity.direction = direction
        self.setTarget(direction)
        self.validDirections = [direction, direction*-1]
        
    def lengthFromNode(self, vector):
        vec = vector - self.node.position
        return vec.magnitudeSquared()

    def overshotTarget(self):
        '''Check if entity has overshot target node'''
        nodeToTarget = self.lengthFromNode(self.target.position)
        nodeToSelf = self.lengthFromNode(self.entity.position)
        return nodeToSelf > nodeToTarget

    def moveTowardsTarget(self, dt):
        '''Move entity towards the target'''
        ds = self.entity.speed*dt
        self.entity.position += DIRECTIONS[self.entity.direction]*ds

    def setTarget(self, direction):
        '''Set a new target based on the direction'''
        self.target = self.node.neighbors[direction]
        
    def reverseDirection(self):
        '''Swap the node and target'''
        temp = self.target
        self.target = self.node
        self.node = temp
        self.entity.direction *= -1

    def removeOppositeDirection(self):
        self.validDirections = self.node.neighbors.keys()
        if self.entity.direction*-1 in self.validDirections:
            if len(self.validDirections) > 1:
                self.validDirections.remove(self.entity.direction*-1)

    def portal(self):
        if self.node.portal:
            self.node = self.node.portal
            self.entity.position = self.node.position
            self.validDirections = self.node.neighbors.keys()
            
    def keyContinuous(self, key):
        '''Listen for directional key presses'''
        if key[K_UP]:
            self.direction = UP
        elif key[K_DOWN]:
            self.direction = DOWN
        elif key[K_RIGHT]:
            self.direction = RIGHT
        elif key[K_LEFT]:
            self.direction = LEFT
        else:
            self.direction = STOP
    
    def keyDiscrete(self, key):
        if key == K_LEFT:
            self.direction = LEFT
        elif key == K_RIGHT:
            self.direction = RIGHT
        elif key == K_UP:
            self.direction = UP
        elif key == K_DOWN:
            self.direction = DOWN


