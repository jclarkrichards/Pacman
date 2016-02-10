"""Will this update if I modify the file directly?"""
from node import NodeGroup
from constants import *

class Level1Nodes(NodeGroup):
    def __init__(self):
        NodeGroup.__init__(self)
        self.file = MAPFILE
        self.createNodeList(self.file)
        self.setPortal()
        
    def setPortal(self):
        self.nodeDict[35].portal = 31 #self.nodeDict[31]
        self.nodeDict[31].portal = 35 #self.nodeDict[35]

    def setPacNode(self):
        '''Set Pacmans start node and position.  Pass into Pacman object'''
        node1 = self.nodeDict[43]
        node2 = self.nodeDict[45]
        position = (node1.position + node2.position) / 2
        return position, 45
    
    def adjustGhostNodes(self):
        '''Some nodes have to be disconnected for the ghosts'''
        self.removeNeighborOneWay(23, 22)
        self.removeNeighborOneWay(25, 24)
        self.removeNeighborTwoWay(23, 25)

    def setHomeNodes(self):
        '''Set the home nodes for all the ghosts'''
        x1, y1 = self.nodeDict[23].position.toTuple()
        x2, y2 = self.nodeDict[25].position.toTuple()
        x, y = ((x1+x2)/2, y1)
        self.addNode((x,y), HOMEBASENODE)
        self.addNode((x, y+48), HOMECENTERNODE)
        self.addNeighborTwoWay(HOMEBASENODE, 23)
        self.addNeighborTwoWay(HOMEBASENODE, 25)
        self.addNeighborTwoWay(HOMEBASENODE, HOMECENTERNODE)

    def setInkyNodes(self):
        x, y = self.nodeDict[HOMECENTERNODE].position.toTuple()
        self.addNode((x-48, y), INKYHOMENODE)
        self.addNode((x-48, y-32), INKYHOMENODE+1)
        self.addNode((x-48, y+32), INKYHOMENODE+2)
        self.addNeighborTwoWay(INKYHOMENODE, HOMECENTERNODE)
        self.addNeighborTwoWay(INKYHOMENODE, INKYHOMENODE+1)
        self.addNeighborTwoWay(INKYHOMENODE, INKYHOMENODE+2)
        self.addHiddenNode(INKYHOMENODE, HOMECENTERNODE)

    def setClydeNodes(self):
        x, y = self.nodeDict[HOMECENTERNODE].position.toTuple()
        self.addNode((x+48, y), CLYDEHOMENODE)
        self.addNode((x+48, y-32), CLYDEHOMENODE+1)
        self.addNode((x+48, y+32), CLYDEHOMENODE+2)
        self.addNeighborTwoWay(CLYDEHOMENODE, HOMECENTERNODE)
        self.addNeighborTwoWay(CLYDEHOMENODE, CLYDEHOMENODE+1)
        self.addNeighborTwoWay(CLYDEHOMENODE, CLYDEHOMENODE+2)
        
    def releaseBlinkyFromHome(self):
        self.clearHiddenNodes(BLINKYHOMENODE)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)
        
    def releasePinkyFromHome(self):
        self.clearHiddenNodes(PINKYHOMENODE)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)
        
    def releaseInkyFromHome(self):
        '''Allow Inky to leave home'''
        self.clearHiddenNodes(INKYHOMENODE)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+1)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)
        
    def releaseClydFromHome(self):
        self.clearHiddenNodes(CLYDEHOMENODE)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+1)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)
        
    def sendBlinkyBackHome(self):
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)
        
    def sendPinkyBackHome(self):
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)
        
    def sendInkyBackHome(self):
        '''Send Inky back home.  Usually after being eaten'''
        self.clearHiddenNodes(INKYHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+1)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)
        
        def sendClydeBackHome(self):
        '''Send Inky back home.  Usually after being eaten'''
        self.clearHiddenNodes(CLYDEHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+1)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)

