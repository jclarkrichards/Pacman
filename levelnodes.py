from node import NodeGroup
from constants import *

LEVELFILE1 = 'maze_test.txt'
PACSTART1 = 43
PACSTART2 = 45
HOMEBASENODE = 100
HOMECENTERNODE = HOMEBASENODE + 1
BLINKYHOMENODE = HOMECENTERNODE
PINKYHOMENODE = HOMECENTERNODE
INKYHOMENODE = HOMECENTERNODE + 1
CLYDEHOMENODE = HOMECENTERNODE + 5


class Level1Nodes(NodeGroup):
    def __init__(self):
        NodeGroup.__init__(self)
        self.createNodeList(LEVELFILE1)
        self.setPortal()
        
    def setPortal(self):
        '''Sets the portal pairs for this level'''
        self.nodeDict[35].portal = 31 
        self.nodeDict[31].portal = 35 


class Level1NodesGhosts(Level1Nodes):
    def __init__(self):
        Level1Nodes.__init__(self)
        self.base = HOMEBASENODE
        
    def removeNodeLinks(self):
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

    def additionalNodes(self):
        pass
    
    def releaseFromHome(self):
        pass
        
    def sendHome(self):
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)

    def resetHomePosition(self):
        return self.nodeDict[self.home].position
        
        
class Level1NodesPacMan(Level1Nodes):
    def __init__(self):
        Level1Nodes.__init__(self)

    def setPacNode(self):
        '''Set Pacmans start node and position.  Pass into Pacman object'''
        node1 = self.nodeDict[PACSTART1]
        node2 = self.nodeDict[PACSTART2]
        position = (node1.position + node2.position) / 2
        return position, 45

    
class Level1NodesClyde(Level1NodesGhosts):
    def __init__(self):
        Level1NodesGhosts.__init__(self)
        self.home = CLYDEHOMENODE

    def reset(self):
        '''Reset to initial conditions'''
        self.clearHiddenNodes(HOMEBASENODE)
        self.clearHiddenNodes(CLYDEHOMENODE)
        self.addHiddenNode(CLYDEHOMENODE, HOMECENTERNODE)
        
    def sendHome(self):
        self.clearHiddenNodes(CLYDEHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+1)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)

    def releaseFromHome(self):
        self.clearHiddenNodes(CLYDEHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+1)
        self.addHiddenNode(CLYDEHOMENODE, CLYDEHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)

    def additionalNodes(self):
        '''Clyde has special nodes only he accesses'''
        x, y = self.nodeDict[HOMECENTERNODE].position.toTuple()
        self.addNode((x+48, y), CLYDEHOMENODE)
        self.addNode((x+48, y-32), CLYDEHOMENODE+1)
        self.addNode((x+48, y+32), CLYDEHOMENODE+2)
        self.addNeighborTwoWay(CLYDEHOMENODE, HOMECENTERNODE)
        self.addNeighborTwoWay(CLYDEHOMENODE, CLYDEHOMENODE+1)
        self.addNeighborTwoWay(CLYDEHOMENODE, CLYDEHOMENODE+2)
        self.addHiddenNode(CLYDEHOMENODE, HOMECENTERNODE)
        
class Level1NodesInky(Level1NodesGhosts):
    def __init__(self):
        Level1NodesGhosts.__init__(self)
        self.home = INKYHOMENODE

    def reset(self):
        '''Reset to initial conditions'''
        self.clearHiddenNodes(HOMEBASENODE)
        self.clearHiddenNodes(INKYHOMENODE)
        self.addHiddenNode(INKYHOMENODE, HOMECENTERNODE)
        
    def sendHome(self):
        self.clearHiddenNodes(INKYHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+1)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, 23)
        self.addHiddenNode(HOMEBASENODE, 25)

    def releaseFromHome(self):
        '''Leave home and prevent from entering'''
        self.clearHiddenNodes(INKYHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+1)
        self.addHiddenNode(INKYHOMENODE, INKYHOMENODE+2)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)

    def additionalNodes(self):
        '''Inky has special nodes only he accesses'''
        x, y = self.nodeDict[HOMECENTERNODE].position.toTuple()
        self.addNode((x-48, y), INKYHOMENODE)
        self.addNode((x-48, y-32), INKYHOMENODE+1)
        self.addNode((x-48, y+32), INKYHOMENODE+2)
        self.addNeighborTwoWay(INKYHOMENODE, HOMECENTERNODE)
        self.addNeighborTwoWay(INKYHOMENODE, INKYHOMENODE+1)
        self.addNeighborTwoWay(INKYHOMENODE, INKYHOMENODE+2)
        self.addHiddenNode(INKYHOMENODE, HOMECENTERNODE)
    
class Level1NodesBlinky(Level1NodesGhosts):
    def __init__(self):
        Level1NodesGhosts.__init__(self)
        self.home = HOMEBASENODE

    def reset(self):
        '''Reset to initial conditions'''
        self.clearHiddenNodes(HOMEBASENODE)
        self.clearHiddenNodes(BLINKYHOMENODE)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)
        
    def releaseFromHome(self):        
        self.clearHiddenNodes(BLINKYHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)


class Level1NodesPinky(Level1NodesGhosts):
    def __init__(self):
        Level1NodesGhosts.__init__(self)
        self.home = PINKYHOMENODE

    def reset(self):
        '''Reset to initial conditions'''
        self.clearHiddenNodes(HOMEBASENODE)
        self.clearHiddenNodes(PINKYHOMENODE)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)

    def releaseFromHome(self):        
        self.clearHiddenNodes(PINKYHOMENODE)
        self.clearHiddenNodes(HOMEBASENODE)
        self.addHiddenNode(HOMEBASENODE, HOMECENTERNODE)


