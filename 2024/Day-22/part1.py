# How to generate a secret magic number

    # Multiply num by 64
    # Bitwise XOR the number
    # Modulus the number by 16777216

    # Divide num by 32
    # Round down to nearest int (assume // does this, be careful if it doesn't)
    # Bitwise XOR and Modulus (16777216) the number

    # Multiply num by 2048
    # Bitwise XOR and modulus (16777216) the number

# Generate 2000 secret numbers (iterations) and return the sum of all numbers' 2000th secret number 
magic_modulus = 16777216
magic_multiply_1 = 64
magic_multiply_2 = 2048
magic_divide = 32

def multiply(num, multiply_by):
    to_mix = num * multiply_by
    #print(f'Creating to_mix: {num} * {multiply_by} = {to_mix}')
    
    mixed_num = num ^ to_mix
    #print(f'Creating mixed_num: {num} ^ {to_mix} = {mixed_num}')

    pruned_num = mixed_num % magic_modulus
    #print(f'Creating pruned_num: {mixed_num} % {magic_modulus} = {pruned_num}\n')
    
    return pruned_num

def divide(num):
    to_mix = num // magic_divide
    #print(f'Creating to_mix: {num} // {magic_divide} = {to_mix}')
    
    mixed_num = num ^ to_mix
    #print(f'Creating to_mix: {num} ^ {to_mix} = {mixed_num}')
    
    pruned_num = mixed_num % magic_modulus
    #print(f'Creating pruned_num: {mixed_num} % {magic_modulus} = {pruned_num}\n')
    
    return pruned_num

magic_numbers = []

with open('input.txt', 'r') as f:
    while True:
        num = f.readline()
        if not num:
            break
        num = int(num)
        for i in range(2000):
            first_num = multiply(num, magic_multiply_1)
            second_num = divide(first_num)
            num = multiply(second_num, magic_multiply_2)
        magic_numbers.append(num)
        
print(sum(magic_numbers))