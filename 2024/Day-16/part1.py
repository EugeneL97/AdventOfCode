# Shortest path finding algorithm
# Something like djikstra's (BFS)
    # Turns are weighted as 1000 while steps are 1
# We go from S to E
    # '#' are walls or obstacles
# Return lowest score (which involves as little turns as possible)
import heapq

def djikstra(maze):
    lowest_score = float('inf')
    pq = [(1, start)]
    visited = set(start)

    while pq:
        _, curr = heapq.heappop(pq)
        visited.add(curr)

        
    return lowest_score

with open('input.txt', 'r') as f:
    maze = [list(line.strip()) for line in f]

start = (1, -2)
end = (-2, 1)
#lowest_score = djikstra(maze)