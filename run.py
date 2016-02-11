import pygame
from pygame.locals import *
from pacman import PacMan
from constants import *
from modeswitcher import ModeSwitcher
from groups import GhostGroup
from levelnodes import Level1Nodes
from pellets import PelletGroup

#class Game(object):
    #def __init__(self):
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = pygame.surface.Surface(SCREENSIZE).convert()
background.fill(BLACK)
nodes = Level1Nodes()
pacman = PacMan(nodes)
clock = pygame.time.Clock()
ghosts = GhostGroup()
gameMode = ModeSwitcher()

pellets = PelletGroup('pellet_map.txt')
pellets.setupPellets()
        
    #def run(self):
while True:
    dt = clock.tick(30) / 1000.0
    
    gameMode.update(dt)

    key_pressed = pygame.key.get_pressed()
    pacman.mover.keyContinuous(key_pressed)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pellets.update(pacman, gameMode)
    ghosts.checkModeChange(gameMode)
    pacman.update(dt)
    ghosts.setGoal(pacman)
    ghosts.update(dt)
    ghosts.checkPacmanCollide(pacman)
    if pellets.numEaten == 40:
        ghosts.inky.releaseFromHome()
        
    screen.blit(background, (0,0))
    nodes.render(screen)
    pellets.render(screen)
    pacman.render(screen)
    ghosts.render(screen)
    pygame.display.update()
            
#game = Game()
#game.run()

