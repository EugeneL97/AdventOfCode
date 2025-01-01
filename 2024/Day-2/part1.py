def is_safe(seq):
    if len(seq) < 2:
        return False 
    diffs = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    # Check if all differences are within the allowed range
    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False
    
    is_increasing = all(d > 0 for d in diffs)
    is_decreasing = all(d < 0 for d in diffs)
    return is_increasing or is_decreasing

with open('input.txt', 'r') as f:
    numbers = [list(map(int, line.strip().split())) for line in f]
    print(numbers[0][0])
safe_reports = sum(is_safe(line) for line in numbers)

print(f"Number of safe reports: {safe_reports}")
