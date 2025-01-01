# Robots patroling on a grid
    # p = (x, y), v = (dx, dy)
    # When they patrol out of bounds they are able to come out the other side of the grid
        # Modulo is probably a good idea here
    # There are 4 quadrants
        # The middle horizontal/vertical line is excluded
    # How many robots are in those quadrants after 100 iterations?
        # How to determine them? They can be overlapped
            # Use the grid position to count how many robots
            # Could do O(m * n) traversal to count
            # OR
            # Data structure to detect which quadrant it is in
                # This might have way too much overhead
                # Checking every robot each iteration, adding, removing into quadrants
                # Rather than a singular scan?

    # Multiply them together for the end result
        # res = q1 * q2 * q3 * q4
rows = 101
cols = 103
iterations = 10000
middle_rows = rows // 2
middle_cols = cols // 2

safety_factors = []

for i in range(iterations):
    q1, q2, q3, q4 = 0, 0, 0, 0
    patrol_grid = [[0] * cols for _ in range(rows)]
    with open('input.txt', 'r') as f:
        while True:
            line = f.readline().split(' ')
            if line == ['']:
                break
            
            position  = line[0].split('=')
            position = position[1].split(',')
            x = int(position[0])
            y = int(position[1])

            velocity = line[1].split('=')
            velocity = velocity[1].split(',')
            dx = int(velocity[0])
            dy = int(velocity[1])

            final_x = (x + i * dx) % rows
            final_y = (y + i * dy) % cols

            patrol_grid[final_x][final_y] += 1
            
            if final_x == middle_rows or final_y == middle_cols:
                continue
            if final_x < middle_rows and final_y < middle_cols:
                #print(f'Adding {final_x} and {final_y} to Quadrant 1!')
                q1 += 1
            if final_x > middle_rows and final_y < middle_cols:
                #print(f'Adding {final_x} and {final_y} to Quadrant 2!')
                q2 += 1
            if final_x < middle_rows and final_y > middle_cols:
                #print(f'Adding {final_x} and {final_y} to Quadrant 3!')
                q3 += 1
            if final_x > middle_rows and final_y > middle_cols:
                #print(f'Adding {final_x} and {final_y} to Quadrant 4!')
                q4 += 1
                
    
    safety_factors.append((q1 * q2 * q3 * q4, i))
print(min(safety_factors)[1])