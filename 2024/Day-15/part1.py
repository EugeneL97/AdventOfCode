# 2D Grid with movable objects and walls
    # Robot: @
    # Objects: O
    # Walls: #
    # Empty grid: .
# Robot can move itself and objects as long as there's no walls
# If a robot or an object is at a wall and the direction makes it move into the wall again
    # Nothing happens
# A whole sequence of moves happen and once we hit the end of all sequences
# Calculate each object's coordinate
    # (100 * y) + x
        # Ex.1: y = 1, x = 4
            # (100 * 1) + 4 = 104
        # Ex.2: y = 100, x = 103
            # (100 * 100) + 103 = 10103
        # Ex.3: y = 0, x = 0
            # (100 * 0) + 0 = 0
# Return the sum of all objects' coordinates given the equation.

# Read the map into a 2D array
# Read the inputs into an array

# Loop through the inputs while updating the map
    # Keep track of the robot('@')'s position for each move

# Since each input is mapped into a direction, i.e. (> = right, or (1,0), moving right on the x once.)
    # Do a while loop to check if there is a chain of objects 
    # Ex.1: (@OOOOO#), we won't move since we see a '#' or a wall
    # Ex.2: (@.OOOO#) -> (.@OOOO#), successful move, if we have another > then we won't move
    # Ex.3: (@OOOO.#) -> (.@OOOO#), successful move, if we have another > then we won't move
    # Ex.4: (.....@#) -> we won't move

