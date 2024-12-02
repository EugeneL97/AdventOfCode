from collections import Counter

with open('input.txt', 'r') as f:
    numbers = f.readlines()
    
    left_side = []
    right_side = []
    
    for num in numbers:
        nums_to_split = num.split()
        
        left_side.append(int(nums_to_split[0]))
        right_side.append(int(nums_to_split[1]))

    
left_side.sort()
right_side.sort()

total_distance = 0
for i in range(len(left_side)):
    total_distance += abs(left_side[i] - right_side[i])

print(total_distance)
