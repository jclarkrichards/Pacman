"""This is a PacMan object that travels from node to node"""
import pygame
from vectors import Vector2D
from pygame.locals import *
#from nodemovement1 import FourWayJump
#from nodemovement2 import FourWayDiscrete
from nodemovement3 import FourWayContinuous
from constants import *

class PacMan(object):
    def __init__(self, position, node):
        self.dim = ENTITYSIZE
        self.COLOR = YELLOW
        self.position = position
        self.speed = SPEED
        self.mover = FourWayContinuous(node, self)
        self.direction = LEFT
        self.radius = 8
        
    def update(self, dt):
        self.mover.update(dt)
        
    def render(self, screen):
        x, y = self.position.toTuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), self.radius)
        #screen.blit(self.frameset[self.iframe], (x-16, y-16))
