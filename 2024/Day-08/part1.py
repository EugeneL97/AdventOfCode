# Read the input and insert it into a 2D array, no splitting necessary

# Find a character X and find its corresponding character in the grid (case sensitivity applies)

# The distance between them is mirrored behind themselves each
    # We don't need to show them on the grid, but if they are out of bounds they do NOT count
        # We need to check their bounds first before we count them
    # Each instance we find is 2, unless they're out of bounds

# Find the distance by determining the difference in x and y position and adding that to both nodes.
    # i.e. If node A is positioned at (1,2) and node B is positioned at (5, 4). The grid is size 10x10
        # The distance between them is (4,2)
        # Node A's antinode would then be (1 - 4, 2 - 2) = (-3, 0), which is out of bounds. This doesn't count
        # Node B's antinode would then be (5 + 4 , 4 + 2) = (9, 6), which is in bounds. This counts
        # Now we have a question, how do we determine the sign of each node...are we adding or subtracting from them?
            # If we swapped node A and node B's signs...(5 - 4, 4 - 2) = (1, 2), (1 + 4, 2 + 2) = (5, 4), they would equal each other.
            # This is not what we want
                # Naive approach is that if their antinode equals to each other, swap the signs and use that
    # Even if the antinode covers a node, it still counts
        # All that matters is if it's out of bounds or not

def parse_input(file):
    with open(file, 'r') as f:
        grid = [line.strip() for line in f]
    return grid

def in_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def find_distance_between_nodes(A_x, A_y, B_x, B_y):
    diff_x = B_x - A_x
    diff_y = B_y - A_y
    return diff_x, diff_y

def find_antinodes(A_x, A_y, B_x, B_y, rows, cols):
    diff_x, diff_y = find_distance_between_nodes(A_x, A_y, B_x, B_y)

    antinode_a = (A_x - diff_x, A_y - diff_y)
    antinode_b = (B_x + diff_x, B_y + diff_y)

    possible_antinodes = []
    if in_bounds(antinode_a[0], antinode_a[1], rows, cols):
        possible_antinodes.append(antinode_a)
    if in_bounds(antinode_b[0], antinode_b[1], rows, cols):
        possible_antinodes.append(antinode_b)

    return possible_antinodes

grid = parse_input('input.txt')
rows = len(grid)
cols = len(grid[0])

counted = [[False for _ in range(cols)] for _ in range(rows)]
antinodes_count = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] != '.':
            char = grid[i][j]
            # Only look for pairs (x, y) > (i, j) to avoid double counting pairs
            for x in range(i, rows):
                # If x == i, start from j+1 to ensure (x, y) > (i, j)
                y_start = j + 1 if x == i else 0
                for y in range(y_start, cols):
                    if grid[x][y] == char:
                        # Get potential antinodes for this pair
                        antinodes = find_antinodes(i, j, x, y, rows, cols)
                        # Count them if not already counted
                        for (ax, ay) in antinodes:
                            if not counted[ax][ay]:
                                counted[ax][ay] = True
                                antinodes_count += 1

print(antinodes_count)
