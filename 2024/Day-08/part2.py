from math import gcd

def parse_input(file):
    with open(file, 'r') as f:
        grid = [line.strip() for line in f]
    return grid

def in_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def line_points(A_x, A_y, B_x, B_y, rows, cols):
    dx = B_x - A_x
    dy = B_y - A_y
    g = gcd(dx, dy)
    dx //= g
    dy //= g

    points = set()

    # Move forward from A
    x, y = A_x, A_y
    while in_bounds(x, y, rows, cols):
        points.add((x, y))
        x += dx
        y += dy

    # Move backward from A
    x, y = A_x, A_y
    while in_bounds(x, y, rows, cols):
        points.add((x, y))
        x -= dx
        y -= dy

    return points

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
                        # Get all line points for this pair
                        pts = line_points(i, j, x, y, rows, cols)
                        for (ax, ay) in pts:
                            if not counted[ax][ay]:
                                counted[ax][ay] = True
                                antinodes_count += 1

print(antinodes_count)
