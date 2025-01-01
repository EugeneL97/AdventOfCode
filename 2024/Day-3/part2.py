# Need to find mul(x,y) instructions
# x and y can both be 1-3 digits [0, 999]
# Sum all valid mul(x,y) as (x * y)

import re

with open('input.txt', 'r') as f:
    text = f.read()

total = 0
do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d+),(\d+)\)"
enabled = True

found_keywords = re.finditer(f'{do}|{dont}|{mul}', text)
for x in found_keywords:
    
    if re.fullmatch(do, x.group()):
        enabled = True
    elif re.fullmatch(dont, x.group()):
        enabled = False
    elif enabled:
        total += int(x.group(1)) * int(x.group(2))    

print(total)