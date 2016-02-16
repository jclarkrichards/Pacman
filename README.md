# Pacman
This will manage my Pacman code so I can see the development process

Pacman and the ghosts move from node to node.  The nodes are the junctions and they are connected together via paths.  The layout of the nodes is contained in the maze.txt file.  The '+' symbols are the nodes and the '-' and '|' are the horizontal and vertical paths respectively.  Each entity has their own copy of the node map which is in the form of a dictionary.  Each node keeps track of its own neighbors and if any of its neighbors are hidden from its view.  The ghosts move automatically and pacman is moved by the player using the directional keys.

Currently in order to start, you need to press the 'h' key.  This is just for testing purposes and will be removed later.  

The pellets have their own text file since that's a lot easier than manually coding in their positions.  In the pellets txt file, 'p' stands for a regular pellet and 'P' stands for a power pellet.  

The ghosts have different modes that they can be in, and they can only be in one mode at a time.  The modes are 'SCATTER', 'ATTACK', FREIGHT', and 'FLEE'.  The game periodically switches between scatter and attack modes.  When pacman eats a power pellet, the ghosts enter freight mode.  If while in freight mode pacman eats them, then the ghosts enter flee mode.  During flee mode they run back home, after which they will enter scatter mode.  After freight mode, the ghosts enter scatter mode and things return to normal.  

==============================================================================
Classes
==============================================================================

Level1Nodes:  Inherits from NodeGroup
-----------
Every level needs to have its own class like this class.  This is just the class for level 1.  If level 2 is different and uses a different map, then a new class will have to be written for Level 2 called Level2Nodes.  This class sets up the dictionary of nodes specific to this level.  The name of the file is defined in the initialization of this class.  Then the 'createNodeList' method is called passing in the file.  The 'createNodeList' method goes through the file an d creates a dictionary of nodes with their neighbors defined.  This dictionary is called nodeDict and has the format of {nodeNum: Node} where nodeNum is an integer indicating a specific Node object.  So saying nodeDict[45] will return the Node object that corresponds to 45.  The 'createNodeList' will also optionally create a text file showing how the nodes are numbered.  This is necessary to know which nodes to start the ghosts and PacMan on.  These values are written into the class that corresponds to the level.

variables
---------
nodeDict:  This is a dictionary of nodes that define the level.  In the form of {nodeVal: Node} where nodeVal is an unique integer that defines a specifc Node object.

methods
-------
setPortal(): returns Nothing
After the node dictionary is created the initialization creates the portal pairs by calling its own 'setPortal' method.  Every node has a 'portal' option which is usually set to None.  Setting it to a node value will create a link with that node.  There can be more than one portal pairs within a level so those are defined here.

setPacNode: returns (Vector2D, Int)
PacMan needs to know where to start.  The nodes he starts on will be different from level to level since each level may have a different set of nodes.  For level 1, for example, he starts between nodes 43 and 45.  So this method calculates the position between these two nodes and returns that vector2D along with the node value 45 since that is his current node even though he is starting half-way between nodes 43 and 45.  He starts the levels moving left always and his current node is always the node he is moving away from.  PacMan's object will call this method in its initilization and receive the starting position and current node value.

adjustGhostNodes: returns Nothing
PacMan and the ghosts have their own node dictionaries which can be independently modified.  After creating the dictionary of nodes from the file, some of the node connections need to be modified for the ghosts.  The nodes that define the ghosts home aren't included in the file so we have to put them in manually.  This method removes the neighbors of the nodes that directly connect to the home nodes.  Also, there are some nodes that are specifically one-way nodes for the ghosts, but not for PacMan.  For example, that means that a ghost can travel from node 23 to node 24, but not from node 24 to node 23.  So we have to remove the neighbor 23 from node 24, but keep the neighbor 24 for node 23.  In the first level there are 4 places where the nodes are one-way nodes for the ghosts.  This is where you indicate those nodes.

setHomeNodes:  returns Nothing
As mentioned above there are some nodes that PacMan doesn't know about and are only for the ghosts.  These are the home nodes.  This is why they are not included in the txt file used to make the initial nodes.  We have to manually connect the home nodes together.  It isn't too bad because there are only a few home nodes.  Before calling this we have to call the 'adjustGhostNodes' method in order to disconnect the two nodes that are directly above the ghosts home since we need to place a node in between them which will connect to the rest of the home nodes.

setInkyNodes: returns Nothing
In addition to the home nodes Inky has a few more nodes that only he knows about.  These are the nodes he bounces between at the start of the levels and also the node that only he returns to when PacMan eats him.  So we define and add those nodes to Inky's node dictionary.

setClydeNodes: returns Nothing
Similar to Inky above, Clyde has some nodes that only he knows about.

sendBlinkyBackHome: returns Nothing
This is called when PacMan eats Blinky.  It clears the hidden nodes that the node at the entrance to the home had so that Blinky can enter the home.  It also hides all other nodes connected to the home entrance node so that when Blinky reaches that node he has no choice but to go inside the home.  All of the other ghosts have similar methods.  sendPinkyBackHome, sendInkyBackHome, sendClydeBackHome.

releaseBlinkyFromHome:  returns Nothing
This is called after PacMan eats Blinky and he returns home.  When he reaches home this method is called.  All it does is clear out the nodes that were hidden previously since those nodes were hidden in order to directly Blinky to his home.  And then it hides the connection to his home so he can't enter it when he's just roaming around normally.  All of the other ghosts have similar methods:  releasePinkyFromHome, releaseInkyFromHome, releaseClydeFromHome.



