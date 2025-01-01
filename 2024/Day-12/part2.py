def find_region_sides(field, x, y, visited):
    rows, cols = len(field), len(field[0])
    region_type = field[x][y]
    stack = [(x, y)]
    cells = []

    horizontal_edges = []
    vertical_edges = []

    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        cells.append((cx, cy))

        # Check neighbors
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or field[nx][ny] != region_type:
                # Boundary edge
                if dx == 0 and dy == 1:
                    # Right edge of (cx, cy)
                    # Vertical line at (cx, cy+1)
                    # We'll store vertical edges as (col, row) so col=cy+1, row=cx
                    vertical_edges.append((cy+1, cx))
                elif dx == 0 and dy == -1:
                    # Left edge of (cx, cy)
                    # Vertical line at (cx, cy)
                    vertical_edges.append((cy, cx))
                elif dx == 1 and dy == 0:
                    # Bottom edge of (cx, cy)
                    # Horizontal line at (cx+1, cy)
                    # We'll store horizontal edges as (row, col) so row=cx+1, col=cy
                    horizontal_edges.append((cx+1, cy))
                else:
                    # Top edge of (cx, cy)
                    # Horizontal line at (cx, cy)
                    horizontal_edges.append((cx, cy))
            else:
                # Same region
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    stack.append((nx, ny))

    area = len(cells)

    # Merge horizontal edges
    # horizontal_edges are stored as (row, col)
    from collections import defaultdict
    horizontal_map = defaultdict(list)
    for r, c in horizontal_edges:
        horizontal_map[r].append(c)
    sides = 0
    for r, cols_list in horizontal_map.items():
        cols_list.sort()
        # Merge consecutive columns
        start = None
        prev = None
        for col_val in cols_list:
            if start is None:
                start = col_val
                prev = col_val
            else:
                if col_val == prev + 1:
                    prev = col_val
                else:
                    # End of one continuous run
                    sides += 1
                    start = col_val
                    prev = col_val
        if start is not None:
            sides += 1

    # Merge vertical edges
    # vertical_edges are stored as (col, row)
    vertical_map = defaultdict(list)
    for c, r in vertical_edges:
        vertical_map[c].append(r)
    for c, rows_list in vertical_map.items():
        rows_list.sort()
        # Merge consecutive rows
        start = None
        prev = None
        for row_val in rows_list:
            if start is None:
                start = row_val
                prev = row_val
            else:
                if row_val == prev + 1:
                    prev = row_val
                else:
                    sides += 1
                    start = row_val
                    prev = row_val
        if start is not None:
            sides += 1

    return area, sides
with open('input.txt') as f:
    field = [list(line.strip()) for line in f]

rows, cols = len(field), len(field[0])
# Main logic assuming 'field' is defined and rows, cols are known
rows, cols = len(field), len(field[0])
visited = [[False]*cols for _ in range(rows)]
total_price = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            area, sides = find_region_sides(field, i, j, visited)
            total_price += (area * sides)

print(total_price)
