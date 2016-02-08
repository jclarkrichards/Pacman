# Pacman
This will manage my Pacman code so I can see the development process

Pacman and the ghosts move from node to node.  The nodes are the junctions and they are connected together via paths.  The layout of the nodes is contained in the maze.txt file.  The '+' symbols are the nodes and the '-' and '|' are the horizontal and vertical paths respectively.  Each entity has their own copy of the node map which is in the form of a dictionary.  Each node keeps track of its own neighbors and if any of its neighbors are hidden from its view.  The ghosts move automatically and pacman is moved by the player using the directional keys.

Currently in order to start, you need to press the 'h' key.  This is just for testing purposes and will be removed later.  

The pellets have their own text file since that's a lot easier than manually coding in their positions.  In the pellets txt file, 'p' stands for a regular pellet and 'P' stands for a power pellet.  

The ghosts have different modes that they can be in, and they can only be in one mode at a time.  The modes are 'SCATTER', 'CHASE', FREIGHT', and 'FLEE'.  The game periodically switches between scatter and chase modes.  When pacman eats a power pellet, the ghosts enter freight mode.  If while in freight mode pacman eats them, then the ghosts enter flee mode.  During flee mode they run back home, after which they will enter scatter mode.  After freight mode, the ghosts enter scatter mode and things return to normal.  


