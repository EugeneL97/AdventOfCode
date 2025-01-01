# Similar to Day 16
# A maze from start (S) to end (E)
# The catch is you can go through TWO walls only
# How many "cheats" can save you at least 100 steps?
    # This means we need a natty way of solving it with no cheats
        # Find that amount (i.e. 250 steps)
        # Now we are looking for methods of 150 steps or less
# Return that amount

# Read in the input data
    # 2D array call it maze
# Find S's position and E's position
    # maze.index('S'), maze.index('E')
# Maybe we do a djikstra's here
    # Weigh walls (only 2 available) as 1. After the 2nd wall, make walls = float('inf') aka BOOM
        # Exit condition when total score is float('inf')
        # Weigh roads higher? (incentivize walls if possible)
            # Do some more research on this method
            # This behavior might just end up running into the walls all the time, and early.
            # Maybe weigh the roads as 1 as well and see how the behavior ends up as 
    # Have a counter for how many steps it's taking and use that to determine our count at the end

