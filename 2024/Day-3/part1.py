# Need to find mul(x,y) instructions
# x and y can both be 1-3 digits [0, 999]
# Sum all valid mul(x,y) as (x * y)

import re

with open('input.txt', 'r') as f:
    text = f.read()

total = 0
mul = r"mul\((\d+),(\d+)\)"

for x, y in re.findall(mul, text):
    total += int(x) * int(y)    

print(total)