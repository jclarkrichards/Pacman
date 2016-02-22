"""Oversees the game and controls it from above.
Receives and sends messages from and to other objects."""
from constants import *

class Observer(object):
    def __init__(self):
        self.timePassed = 0

    def sendGhostHome(self):
        pass

    def releaseGhostFromHome(self):
        pass

    def checkForPacDeath(self, pacman):
        if not pacman.alive:
            return True
        return False
    
    def checkForEndGame(self, pellets):
        '''End the game if all the pellets have been eaten'''
        if pellets.numEaten == pellets.numMax:
            return True
        return False

    def startGame(self, dt): #mode):
        self.timePassed += dt
        if self.timePassed >= 3:
        #if mode != START:
            return True
        return False

    def checkForRelease(self, ghosts, numPellets):
        '''Release a ghost when it is equal to numPellets'''
        ghostlist = [g for g in ghosts if not g.released]
        for ghost in ghostlist:
            if ghost.valueForRelease == numPellets:
                ghost.releaseFromHome()
                ghost.released = True

    #def doReverseGhosts(self, powerEaten, mode):
    #    '''Tell the ghosts to reverse direction if a power pellet
    #    was eaten or a mode change to attack occurred.'''
    #    if powerEaten or (mode.mode == ATTACK and mode.modeChange == True):
    #        if powerEaten:
    #            mode.setMode(FREIGHT)
    #        return True
    #    return False

    def updateSpeed(self, pacman, ghosts):
        '''Any speed modifiers would go here.  Or rather if there were
        any speed modifiers then this should tell the ghosts and 
        the ghosts will modify the speed.'''
        pass
        #test = ghosts.blinky.position - pacman.position
        #if test.magnitudeSquared() <= 2400:
        #    pacman.speed = SPEED + 50
        #else:
        #    pacman.speed = SPEED


