# Overview
    # Generally speaking, group letters and determine their region, BFS
    # We calculate the perimeter and area of a region
        # Perimeter = Fencing required for that region
            # If an X is in the middle of a field of Y's, it will take 4 fences to cover a single X
            # Anytime we hit out of bounds or a crop (char) that isn't our own, that is one fencing required
        # Area = Total count of crops in our region (i.e. X or Y)
    # When we multiply perimeter and area of our region, we get the cost of the fencing
    # We sum up the total cost of the fencing 

# Read the file input
    # Output it into a 2D array
# Create a visited array for fields we already explored
# Start at field[0][0]
    # find_fences(field, 0, 0)
        # if field[x][y] == 0:
            # return 0, 0
        # if 0 < x < len(field) and 0 < y < len(field[0]) and char != field[x][y]:
            # return 0, 1
        # # Use this as a visited
        # field[x][y] = '0'
        # area = 1
        # perimeter = 0 
        # directions = [(1,0), (0,1), (-1,0), (0,-1)]
        # for dx, dy in directions:
            # unpacked_area, unpacked_perimeter = find_fences(field, x + dx, y + dy)
            # area += unpacked_area
            # perimeter += unpacked_perimeter
        # return area, perimeter

# fencing_cost = 0
# for x in range(rows):
    # for y in range(cols):
        # if field[x][y] != '0':
            # area = 0

            # area, perimeter = find_fences(field, area, x, y)
            # fencing_cost += (area * perimeter)
# return fencing_cost
def find_fences(field, curr_sub_field, x, y, local_visited):
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return 0, 1
    if local_visited[x][y]:
        return 0, 0
    if field[x][y] != curr_sub_field:
        return 0, 1

    local_visited[x][y] = True

    area = 1
    perimeter = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        sub_area, sub_perimeter = find_fences(field, curr_sub_field, nx, ny, local_visited)
        area += sub_area
        perimeter += sub_perimeter

    return area, perimeter


with open('input.txt') as f:
    field = [list(line.strip()) for line in f]

rows, cols = len(field), len(field[0])
visited = [[False] * cols for _ in range(rows)]
global_visited = [[False] * cols for _ in range(rows)]

fencing_cost = 0

for x in range(rows):
    for y in range(cols):
        if not global_visited[x][y]:
            # Start of a new region
            curr_sub_field = field[x][y]
            local_visited = [[False] * cols for _ in range(rows)]
            area, perimeter = find_fences(field, curr_sub_field, x, y, local_visited)
            
            # Mark all visited cells from this region globally
            for i in range(rows):
                for j in range(cols):
                    if local_visited[i][j]:
                        global_visited[i][j] = True
            
            fencing_cost += area * perimeter

print(fencing_cost)
