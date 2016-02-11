from constants import *

class ModeSwitcher(object):
    def __init__(self):
        self.setMode(SCATTER)
        self.modeChange = False

    def update(self, dt):
        self.timeEllapsed += dt
        self.modeChange = False
        if self.mode == SCATTER and self.timeEllapsed >= SCATTERTIME:
            self.setMode(ATTACK)
        elif self.mode == ATTACK and self.timeEllapsed >= ATTACKTIME:
            self.setMode(SCATTER)
        elif self.mode == FREIGHT and self.timeEllapsed >= FREIGHTTIME:
            self.setMode(SCATTER)
        elif self.mode == START and self.timeEllapsed >= STARTTIME:
            self.setMode(SCATTER)

    def setMode(self, mode):
        self.mode = mode
        self.modeChange = True
        self.timeEllapsed = 0
