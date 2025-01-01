# Overview:
    # DFS from position 0 (trailhead) to position 9 (peak).
        # Each unique peak (9) per trailhead counts towards our result
    # This means we look up, down, left, right. We only go either direction when it's an increment of 1 of our current position
        # Ex.1: 0 -> 1 -> 2 -> ... -> 9. This would count as a plausible trail!
        # Ex.2: 0 -> 2 would not work as it jumps from 0 to 2. We don't have climbing gear!
    # If one trailhead is connected to 5 different peaks, this is 5.
        # Until we run out of trailheads we'll gather a sum of all of them.

# Read the file input into a 2D Array
    # Start dfs only where the position is 0
        # If up, down, left, or, right are not incremented by 1, hit the base case
            # When we find a 9, add that 9's coordinates in our visited set
            # We only increment by 1 if that 9 has not been visited
            # We create a new visited set for each trailhead
        # If we visit a visited 9, hit the base case
        # Once we exhaust all possibilities, sum this to our total

def read_file_input(file):
    with open(file, 'r') as f:
        arr = [list(map(int, line.strip())) for line in f]
    return arr

def find_peaks_visited(topographic_map):
    total = 0

    for x in range(rows):
        for y in range(cols):
            if topographic_map[x][y] == 0:
                total += dfs(x, y)

def dfs(x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # TODO: Add a visited set for each initial dfs call and add 9 to it
    for dx, dy in directions:
        if in_bounds(x + dx, y + dy):
            dfs(x + dx, y + dy)
    return 1

def in_bounds(x, y):
    if 0 <= x < rows and 0 <= y < cols:
        return True
    return False

topographic_map = read_file_input('input.txt')
rows = len(topographic_map)
cols = len(topographic_map[0])

peaks_visited = find_peaks_visited(topographic_map)

print(peaks_visited)
