import pygame
from pygame.locals import *
from pacman import PacMan
from constants import *
from modeswitcher import ModeSwitcher
from groups import GhostGroup
from levelnodes import Level1NodesPacMan
from pellets import PelletGroup
from gamecontrol import Observer

#class Game(object):
    #def __init__(self):
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = pygame.surface.Surface(SCREENSIZE).convert()
background.fill(BLACK)
nodes = Level1NodesPacMan() #similar for level2, 3, 4, etc...
pacman = PacMan(nodes)
clock = pygame.time.Clock()
ghosts = GhostGroup()
gameMode = ModeSwitcher()

pellets = PelletGroup('pellet_map.txt')
pellets.setupPellets()

control = Observer()
    #def run(self):
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    dt = clock.tick(30) / 1000.0
    gameMode.update(dt)
    key_pressed = pygame.key.get_pressed()
    pacman.mover.keyContinuous(key_pressed)
    if control.checkForEndGame(pellets):
        pacman.reset()
        ghosts.reset()
        gameMode.reset()
        pellets.reset()
        
    if control.startGame(gameMode.mode):
        control.checkForRelease(ghosts.members, pellets.numEaten)
        powerEaten = pellets.checkCollided(pacman)
        if control.doReverseGhosts(powerEaten, gameMode):
            ghosts.reverseDirection()
        ghosts.checkModeChange(gameMode)
        pacman.update(dt)
        ghosts.setGoal(pacman)
        ghosts.update(dt)
        ghosts.checkPacmanCollide(pacman)
        

    screen.blit(background, (0,0))
    nodes.render(screen)
    pellets.render(screen)
    pacman.render(screen)
    ghosts.render(screen)
    pygame.display.update()
            
#game = Game()
#game.run()

