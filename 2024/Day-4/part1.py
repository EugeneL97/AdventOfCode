# Must find instances of XMAS, not just one
# Search up, down, left, right, diagonal
    # Omnidirectional DFS
# Turn input.txt into an indexable 2D array of strings
with open ('input.txt', 'r') as f:
    word_search = [line.strip() for line in f]

goal_word = ['X', 'M', 'A', 'S']

for x in range(len(word_search[0])):
    for y in range(len(word_search[1])):
        if word_search[x][y] == 'X':
            
            print(f'Found x at ({x}, {y})!')
# def dfs():
#     if x + 1, y
    