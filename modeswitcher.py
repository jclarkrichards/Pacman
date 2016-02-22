"""Keeps track of how much time has passed in each mode and will switch the mode if the time exceeds the allowed mode time.  
Can also switch modes early with setMode"""
from constants import *

class ModeSwitcher(object):
    def __init__(self):
        self.modes = {ATTACK:Attack(), SCATTER:Scatter(), FREIGHT:Freight(), FLEE:Flee()}
        self.modeVal = SCATTER
        self.mode = None
        self.timeEllapsed = 0
        self.setMode(self.modeVal) #START)
        self.modeChange = False

    def update(self, dt, powerPellet=False, reachedHome=False):
        self.timeEllapsed += dt
        self.modeChange = False
        if self.modeVal != FLEE:
            if self.timeEllapsed >= self.mode.time:
                self.setMode(self.mode.setNextMode(powerPellet))
        else:
            if reachedHome:
                self.setMode(self.mode.setNextMode())
                
        #if self.mode == SCATTER and self.timeEllapsed >= SCATTERTIME:
        #    self.setMode(ATTACK)
        #elif self.mode == ATTACK and self.timeEllapsed >= ATTACKTIME:
        #    self.setMode(SCATTER)
        #elif self.mode == FREIGHT and self.timeEllapsed >= FREIGHTTIME:
        #    self.setMode(SCATTER)
        #elif self.mode == START and self.timeEllapsed >= STARTTIME:
        #    self.setMode(SCATTER)

    def setMode(self, mode):
        self.modeVal = mode
        self.mode = self.modes[mode] #mode
        self.modeChange = True
        self.timeEllapsed = 0

    def overideMode(self):
        '''Set the mode to FLEE only if the mode is in FREIGHT'''
        if not self.inFleeMode():
            if self.inFreightMode():
                self.setMode(FLEE)
                return True
        return False
        
    def reset(self):
        '''Reset to initial conditions'''
        self.modeVal = SCATTER
        self.setMode(self.modeVal) #START)
        self.modeChange = False
        
    def inFreightMode(self):
        if self.modeVal == FREIGHT:
            return True
        return False
        
    def inFleeMode(self):
        if self.modeVal == FLEE:
            return True
        return False
        


class Attack(object):
    def __init__(self):
        self.speed = 100
        self.time = 20
        
    def setNextMode(self, powerPellet=False):
        if powerPellet:
            return FREIGHT
        return SCATTER
    
    def setGoal(self, ghost, pacman, blinky=None):
        ghost.attack(pacman, blinky)
    
class Scatter(object):
    def __init__(self):
        self.speed = 100
        self.time = 7
    
    def setNextMode(self, powerPellet=False):
        if powerPellet:
            return FREIGHT
        return ATTACK
    
    def setGoal(self, ghost, pacman=None, blinky=None):
        ghost.scatter()
    
class Freight(object):
    def __init__(self):
        self.speed = 50
        self.time = 5
    
    def setNextMode(self, powerPellet=False):
        return SCATTER
    
    def setGoal(self, ghost, pacman=None, blinky=None):
        ghost.freight()
    
class Flee(object):
    def __init__(self):
        self.speed = 150
        self.time = 0  #depends on ghost reaching home, not time
    
    def setNextMode(self, powerPellet=False):
        return SCATTER

    def setGoal(self, ghost, pacman=None, blinky=None):
        ghost.flee()
