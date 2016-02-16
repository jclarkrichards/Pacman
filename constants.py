"""Contains values that every level uses and these values do not change"""
from vectors import Vector2D

#Setup
MAPWIDTH = 28
MAPHEIGHT = 36
TILEWIDTH = 16
TILEHEIGHT = 16
WIDTHPX = MAPWIDTH * TILEWIDTH
HEIGHTPX = MAPHEIGHT * TILEHEIGHT

#Sizes
SCREENSIZE = (WIDTHPX, HEIGHTPX)
ENTITYSIZE = (TILEWIDTH, TILEHEIGHT)

#Entity speeds
SPEED = 100
FREIGHTSPEED = 50
FLEESPEED = 150

#Ghost Constants
TILES4 = TILEWIDTH * 4
TILES8 = TILEWIDTH * 8
TILES8SQ = TILES8*TILES8

#Ghost Scatter Positions
BLINKYGOAL = Vector2D(WIDTHPX-48, 0)
PINKYGOAL = Vector2D(48, 0)
INKYGOAL = Vector2D(WIDTHPX, HEIGHTPX-32)
CLYDEGOAL = Vector2D(0, HEIGHTPX-32)

#Modes for the ghosts
SCATTER = 0
ATTACK = 1
FREIGHT = 2
FLEE = 3
START = 4
PAUSE = 5

#Time in seconds for each mode
SCATTERTIME = 7
ATTACKTIME = 20
FREIGHTTIME = 5
STARTTIME = 3

#Direction Unit Vectors
UP = 1
DOWN = UP*-1
LEFT = 2
RIGHT = LEFT*-1
STOP = 0

DIRECTIONS = {UP:Vector2D(0,-1), DOWN:Vector2D(0,1),
              LEFT:Vector2D(-1,0), RIGHT:Vector2D(1,0),
              STOP:Vector2D()}

POWERPELLET = True

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (250,0,250)
TEAL = (0,255,255)

