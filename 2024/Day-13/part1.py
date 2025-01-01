# Cramer's Rule
# Button A: X + 94, Y + 34
# Button B: X + 22, Y + 67
#           X=8400, Y = 5400

# A = |94 22| = b|8400| -> x1 x2 = x3
# A = |34 67| = b|5400| -> y1 y2 = y3

#          (x1)(y2) - (x2)(y1) 
# det(A) = (94)(67) - (22)(34) = 6298 - 748 = 5550  

# det(A_p) = A_p = |8400 22|
#                  |5400 67|
#            ( b1 )(y2) - (x2)( b2 )
# det(A_p) = (8400)(67) - (22)(5400) = 562800 - 118800 = 444000

# det(A_q) = |94 8400|
#            |34 5400|
#            (x1)( b2 ) - (y1)( b1 )
# det(A_q) = (94)(5400) - (34)(8400) = 507600 - 285600 = 222000

# p = det(A_p) / det(A) = 444000 / 5550 = 80
# q = det(A_q) / det(A) = 222000 / 5550 = 40

# 94(80) + 22(40) = 7520 + 880 = 8400
# 34(80) + 67(40) = 2720 + 2680 = 5400

# Button A + Button B presses
# 3(80) + 1(40) = 280 tokens 

# Read file input
# Every 4 lines it's a new problem

# Line Block Structure
# Line 1: 'Button A: X + x_1, Y + y_1
# Line 2: 'Button B: X + x_2, Y + y_2
# Line 3: 'Prize: X=x_total, Y=y_total
# Line 4: '\n'

# Next steps:
# Line 1: Extract 'x_1' and 'y_1'
# Line 2: Extract 'x_2' and 'y_2'
# Line 3: Extract 'x_total' and 'y_total'
# Line 4: Nothing to extract

# Strip white space first
    # Split at the ':'
    # Split at the ',

# How are we going to parse all of these?
# As tuples and store into a list?
# Treat each problem as an iteration in a for loop?
# Have each tuple at i position correlate with problem i
import math

def parse_line(line):
    _, values = line.split(':')
    x_part, y_part = values.split(',')

    x_value = int(x_part.split('+')[1]) if '+' in x_part else int(x_part.split('=')[1])
    y_value = int(y_part.split('+')[1]) if '+' in y_part else int(y_part.split('=')[1])
    return x_value, y_value

questions = []
with open('input.txt') as f:
   while True:

    line1 = f.readline().strip()
    # End of list
    if not line1:
      break
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    # Skip the newline
    line4 = f.readline()

    button_a = parse_line(line1) 
    button_b = parse_line(line2)
    prize = parse_line(line3) 
    
    questions.append([*button_a, *button_b, *prize])

token_total = 0
for question in questions:
    
    x_1, y_1, x_2, y_2, b_1, b_2 = question

    det = (x_1 * y_2) - (x_2 * y_1)
    det_p = (b_1 * y_2) - (x_2 * b_2)
    det_q = (x_1 * b_2) - (b_1 * y_1)
    
    p = det_p / det
    q = det_q / det

    # Screen out negative and decimal numbers (unsolvable)
    if p != math.trunc(p) or q != math.trunc(q) or p < 0 or q < 0:
       continue
    token_total += (3 * p) + q

print(int(token_total))
