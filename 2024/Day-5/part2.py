from collections import defaultdict, deque

def parse_input_file(filename):
    """
    Parses the input file and separates the ordering rules and updates.

    :param filename: The name of the input file.
    :return: A tuple containing the list of ordering rules and the list of updates.
    """
    ordering_rules = []
    updates = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        # Find the index where the updates start (empty line indicates separation)
        for i, line in enumerate(lines):
            if line.strip() == '':
                break
        else:
            i = len(lines)  # No empty line found; all lines are ordering rules

        # Parse ordering rules
        ordering_rules = parse_ordering_rules(lines[:i])

        # Parse updates
        updates = parse_updates(lines[i+1:])

    return ordering_rules, updates

def parse_ordering_rules(lines):
    """
    Parses the ordering rules from the given lines.

    :param lines: List of lines containing ordering rules.
    :return: A list of tuples representing the ordering rules.
    """
    ordering_rules = []
    for line in lines:
        if '|' in line:
            x, y = map(int, line.strip().split('|'))
            ordering_rules.append((x, y))
    return ordering_rules

def parse_updates(lines):
    """
    Parses the updates from the given lines.

    :param lines: List of lines containing updates.
    :return: A list of lists, where each sublist is an update sequence.
    """
    updates = []
    for line in lines:
        if ',' in line:
            update = list(map(int, line.strip().split(',')))
            updates.append(update)
    return updates

def build_page_to_rules_map(ordering_rules):
    """
    Builds a mapping from pages to the rules they are involved in.

    :param ordering_rules: A list of tuples representing the ordering rules.
    :return: A defaultdict mapping pages to lists of ordering rules.
    """
    page_to_rules = defaultdict(list)
    for x, y in ordering_rules:
        page_to_rules[x].append((x, y))
        page_to_rules[y].append((x, y))
    return page_to_rules

def is_update_valid(update, page_indices, ordering_rules):
    """
    Determines if an update sequence is valid according to the ordering rules.

    :param update: The update sequence as a list of pages.
    :param page_indices: A dictionary mapping pages to their indices in the update.
    :param ordering_rules: A list of all ordering rules.
    :return: True if the update is valid, False otherwise.
    """
    checked_rules = set()
    page_to_rules = build_page_to_rules_map(ordering_rules)
    for page in update:
        if page in page_to_rules:
            for rule in page_to_rules[page]:
                if rule in checked_rules:
                    continue  # Avoid checking the same rule multiple times
                checked_rules.add(rule)
                x, y = rule
                if x in page_indices and y in page_indices:
                    if page_indices[x] >= page_indices[y]:
                        return False  # Invalid update
    return True  # Valid update

def topological_sort(pages, ordering_rules):
    """
    Performs a topological sort on the given pages according to the ordering rules.

    :param pages: A list of pages to sort.
    :param ordering_rules: A list of ordering rules as tuples (X, Y).
    :return: A list of pages in a valid order, or None if a cycle is detected.
    """
    adjacency_list = defaultdict(list)
    in_degree = defaultdict(int)

    # Initialize in-degree of all pages to 0
    for page in pages:
        in_degree[page] = 0

    # Add edges based on ordering rules
    for x, y in ordering_rules:
        if x in pages and y in pages:
            adjacency_list[x].append(y)
            in_degree[y] += 1

    # Queue for pages with in-degree 0
    queue = deque([page for page in pages if in_degree[page] == 0])

    sorted_pages = []

    while queue:
        current_page = queue.popleft()
        sorted_pages.append(current_page)
        for neighbor in adjacency_list[current_page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_pages) != len(pages):
        # Cycle detected; ordering not possible
        return None

    return sorted_pages

def calculate_corrected_middle_pages(updates, ordering_rules):
    """
    Corrects the invalid updates by ordering them according to the rules and
    calculates the total sum of their middle pages.

    :param updates: A list of update sequences.
    :param ordering_rules: A list of all ordering rules.
    :return: The total sum of middle pages from corrected invalid updates.
    """
    total_middle_pages = 0
    for update in updates:
        # Create a page index mapping for the current update
        page_indices = {page: idx for idx, page in enumerate(update)}
        # Check if the update is valid
        if is_update_valid(update, page_indices, ordering_rules):
            # Skip valid updates; only process invalid ones
            continue
        # Perform topological sort to get the corrected order
        sorted_update = topological_sort(update, ordering_rules)
        if sorted_update is None:
            # Cycle detected; skip this update or handle as needed
            pass  # You can handle cycles differently if needed
        else:
            # Find the middle page and add to total
            middle_index = len(sorted_update) // 2
            middle_page = sorted_update[middle_index]
            total_middle_pages += middle_page
    return total_middle_pages

# Parse the input file
filename = 'input.txt'  # Replace with your input file name
ordering_rules, updates = parse_input_file(filename)

# Calculate the total sum of middle pages from corrected invalid updates
total_middle_pages = calculate_corrected_middle_pages(updates, ordering_rules)

# Output the result
print(f"Total sum of middle pages from corrected invalid updates: {total_middle_pages}")

