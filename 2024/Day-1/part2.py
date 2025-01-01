from collections import Counter

with open('input.txt', 'r') as f:
    numbers = f.readlines()
    
    left_side = []
    right_side = []
    
    for num in numbers:
        nums_to_split = num.split()
        
        left_side.append(int(nums_to_split[0]))
        right_side.append(int(nums_to_split[1]))


right_side = Counter(right_side)

similiarity_sum = 0
# if 3 is in left_side, multiply it by the counter of 3 in right_side
for i in range(len(left_side)):
    if left_side[i] in right_side:
        similiarity_sum += left_side[i] * right_side[left_side[i]]
print(similiarity_sum)