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
part2 = 10000000000000
for question in questions:
    
    x_1, y_1, x_2, y_2, b_1, b_2 = question
    
    b_1 += part2
    b_2 += part2
    
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