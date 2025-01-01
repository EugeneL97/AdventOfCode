with open('input.txt', 'r') as f:
    lines = f.readlines()
    numbers = [list(map(int, line.strip().split())) for line in lines]

def is_sequence_safe(seq):
    if len(seq) < 2:
        return False
    diffs = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    is_increasing = all(d > 0 for d in diffs)
    is_decreasing = all(d < 0 for d in diffs)
    if not (is_increasing or is_decreasing):
        return False
    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False
    return True

def is_safe_report(line):
    if is_sequence_safe(line):
        return True
    for i in range(len(line)):
        new_seq = line[:i] + line[i+1:]
        if is_sequence_safe(new_seq):
            return True
    return False

safe_reports = sum(is_safe_report(line) for line in numbers)

print(f"Number of safe reports: {safe_reports}")