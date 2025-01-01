# Process the file where the first value is the sum of the numbers following the colon
    # You must determine if we add or multiply the numbers to make the sum possible
    # Therefore, we have to exhaust all possible combinations of + or * for each number in the line to see if they match our sum
    # We will terminate and check only at the end of the loop
        # We can't find the sum early, that's not valid
    # We need at most, one valid combination, as more than that will not affect the answer
        # Help computation time too, granted this is already a brute force approach
    # We will sum all the sums for our final answer

def parse_input_file(file):
    with open(file, 'r') as f:
        input = [[int(value) for value in line.strip().replace(':', ' ').split()] for line in f]
    return input

def find_total_calibration_result(numbers):
    calibration_result = 0

    for line in numbers:
        target = line[0]

        calibration_result += can_reach_target_sum(target, line[1:])

    return calibration_result

def concatenate_numbers(num1, num2):
    num_digits = len(str(num2))
    
    return num1 * (10 ** num_digits) + num2

def can_reach_target_sum(target, numbers):
    dp = {numbers[0]}

    for i in range(1, len(numbers)):
        next_set = set()

        for num in dp:
            for result in (
                num + numbers[i],
                num * numbers[i],
                num * (10 ** len(str(numbers[i]))) + numbers[i]
            ):  
                if result <= target:
                    next_set.add(result)

        dp = next_set

    return target if target in dp else 0

input = parse_input_file('input.txt')

calibration_result = find_total_calibration_result(input)

print(calibration_result)