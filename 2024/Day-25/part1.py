# Locks 
    # Height of 6
    # Lock starts with a row of '#' on top
    # Key starts with a row of '#' on bottom
        # Depending on if it's a lock or a key, the bottom or top is an empty row of '.''s
    # If Lock + Key > 5 for any given column
        # Key is invalid for the lock
    # If Lock + Key <= 5 for any given column
        # Key is valid for the lock
    # Count how many valid keys for locks

# Read the file input
    # If the first row is dots, it's a key
    # If the first row is hashes, it's a lock
    # key = [], lock = []
        # Store the values of how many hashes are in each column
    # Read 6 lines then EOL and repeat until EOF


# Brute force O(m * n), m = key, n = locks    
    # For every key, try every lock
    # If key[column] + lock[column] <= 5, keep going
        # If at any point it's > 5, end early and don't total it
        

# Total up all valid unique combinations of locks and keys

with open('input.txt', 'r') as f:
    keys, locks = [], []
    while True:

        temp_lines = [f.readline().strip() for _ in range(8)]
        temp_lines = [line for line in temp_lines if line]
        if not temp_lines:
            break
        
        hash_counter = [-1 for _ in range(5)]
        for line in temp_lines:
            for i, char in enumerate(line):
                if char == '#':
                    hash_counter[i] += 1
                    
        if '.' in temp_lines[0]:
            keys.append(hash_counter)
        elif '#' in temp_lines[0]:
            locks.append(hash_counter)
        
        
print(f'{keys} \n\n {locks}')

valid_locks = 0
for key in keys:
    for lock in locks:
        invalid_combo = False
        for i in range(5):
            if key[i] + lock[i] > 5:
                invalid_combo = True
                break
        if not invalid_combo:
            valid_locks += 1
print(f'Valid locks: {valid_locks}')