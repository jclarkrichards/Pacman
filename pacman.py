"""This is a PacMan object that travels from node to node"""
import pygame
from vectors import Vector2D
from pygame.locals import *
from nodemovement3 import FourWayContinuous
from constants import *

class PacMan(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.COLOR = YELLOW
        #self.direction = LEFT
        self.reset()
        self.radius = 8
        
    def update(self, dt):
        self.mover.update(dt)

    def reset(self):
        self.direction = LEFT
        self.position, nodeVal = self.nodes.setPacNode()
        self.mover = FourWayContinuous(self.nodes, nodeVal, self)
        self.speed = SPEED
        self.alive = True
        
    def render(self, screen):
        x, y = self.position.toTuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), self.radius)
        #screen.blit(self.frameset[self.iframe], (x-16, y-16))
