# Process the file into a 2D array
# Find the caret(^)
    # Traverse upwards until you hit '#', instead turn 90 degrees clockwise (right)
    # As you traverse, mark the visited locations with an 'X'.
        # Keep count of total 'X's, you will return this later
        # If it's already an 'X', don't count it
    # As soon as you get out of bounds (x > len(graph[0]) or y > len(graph[1]) or x < 0 or y < 0) of the array, terminate the loop and return the total number of X's
def process_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
def total_distinct_positions_visited(map):
    
guard_patrol = process_input('input.txt')


#print(total_distinct_positions_visited(guard_patrol))