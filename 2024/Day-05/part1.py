# {X|Y} X must be printed before Y in the page ordering rules
# When looking at the line by line input after the page ordering rules
    # You confirm that that sequence adheres to the page ordering rules
        # 61|32
        # 23|53
        # (61, 32, 53)
        # This line is true because 61 goes before 32. There is no 23, so that check is ignored.
        # Valid Line
            #If it's a valid line, find the middle value of the array and sum their totals

# We parse both styles of input
    # Page Ordering Rules have a pipe .split('|')
        # Split into a tuple, since they're always size 2
    # Pages have commas .split(',')
        # Split into an indexable array

# Store the values into a hash table?
    # O(n^2)
        # We will look at the i index and compare it to against all indexes except i
            # i.e. i = 2, len(line) = 5: 0, 1, 3, 4 are the indexes we look at
        # Note their index position relative to i.
        # We would search for keys and values separately since they dictate order
            # i.e. (75|14)
            #      (14|53)
            #      75,14,53 - For the first rule, 14 is in values, compare it against its key
            #                 For the second rule, 14 is in keys, compare it against its value
from collections import defaultdict

def parse_input(file):
    ordering_rules = []
    updates = []
    
    with open(file, 'r') as f:
        lines = f.readlines()
        
        for separation_idx, line in enumerate(lines):
            # Found the separation_idx when ordering_rules transition to updates
            if line.strip() == '':
                break
            
    ordering_rules = parse_ordering_rules(lines[:separation_idx])
    updates = parse_updates(lines[separation_idx+1:])
    
    return ordering_rules, updates

def parse_ordering_rules(lines):
    ordering_rules = []

    for line in lines:
        if '|' in line:
            x, y = map(int, line.strip().split('|'))
            ordering_rules.append((x, y))
    
    return ordering_rules

def parse_updates(lines):
    updates = []

    for line in lines:
        if ',' in line:
            update = list(map(int, line.strip().split(',')))
            updates.append(update)

    return updates

def build_page_to_rules_map(ordering_rules):
    page_to_rules = defaultdict(list)

    for x, y in ordering_rules:
        page_to_rules[x].append((x, y))
        page_to_rules[y].append((x, y))

    return page_to_rules
def is_update_valid(update, page_indices, page_to_rules):
    checked_rules = set()
    for page in update:
        if page in page_to_rules:
            for rule in page_to_rules[page]:
                if rule in checked_rules:
                    continue
                checked_rules.add(rule)
                x, y = rule
                if x in page_indices and y in page_indices:
                    if page_indices[x] >= page_indices[y]:
                        return False
    return True
def calculate_sum_middle_pages(updates, page_to_rules):
    total_middle_pages = 0

    for update in updates:
        page_indices = {page: idx for idx, page in enumerate(update)}

        if is_update_valid(update, page_indices, page_to_rules):
            middle_idx = len(update) // 2
            middle_page = update[middle_idx]
            total_middle_pages += middle_page

    return total_middle_pages

ordering_rules, updates = parse_input('input.txt')

page_to_rules = build_page_to_rules_map(ordering_rules)

total_middle_pages = calculate_sum_middle_pages(updates, page_to_rules)

print(f"Total sum of middle pages: {total_middle_pages}")