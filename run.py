import pygame
from pygame.locals import *
from pacman import PacMan
from constants import *
#from modeswitcher import ModeSwitcher
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
#gameMode = ModeSwitcher()

pellets = PelletGroup('pellet_map.txt')
pellets.setupPellets()

control = Observer()
    #def run(self):
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    dt = clock.tick(30) / 1000.0
    #gameMode.update(dt)
    
    key_pressed = pygame.key.get_pressed()
    pacman.mover.keyContinuous(key_pressed)
    
    ghosts.checkPacmanCollide(pacman)
    if control.checkForPacDeath(pacman):
        pacman.reset()
        ghosts.reset()
        gameMode.reset()
        
    if control.checkForEndGame(pellets):
        pacman.reset()
        ghosts.reset()
        gameMode.reset()
        pellets.reset()
        
    if control.startGame(dt): #gameMode.mode):
        control.checkForRelease(ghosts.members, pellets.numEaten)
        powerEaten = pellets.checkCollided(pacman)
        #if control.doReverseGhosts(powerEaten, gameMode):
        #    ghosts.reverseDirection()
        ghosts.modeUpdate(dt, powerEaten)
        #ghosts.checkModeChange() #gameMode) #reverse the ghosts here if the mode changed.  Part of mode update?

        control.updateSpeed(pacman, ghosts) #based on mode or other factors
        pacman.update(dt)
        #ghosts.setGoal(pacman) #Should be a part of the ghosts mode update?
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

