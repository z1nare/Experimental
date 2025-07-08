from collections import defaultdict, deque

# Read the input file
pages = []
with open("C:\\Users\\garba\\Downloads\\adventcode.csv", "r") as file:
    for line in file:
        pages.append(line.strip())

# Split the input into rules and updates
rules = pages[:1177]
actuals = pages[1177:]

# Parse rules into a dictionary
order = defaultdict(list)
for rule in rules:
    parts = rule.split("|")
    if len(parts) == 2:
        x, y = parts
        order[x].append(y)

# Function to check if an update is valid
def is_valid_order(update, order):
    update_pages = update.split(",")
    page_positions = {page: idx for idx, page in enumerate(update_pages)}
    
    for page, must_follow in order.items():
        if page in page_positions:
            for follower in must_follow:
                if follower in page_positions and page_positions[page] > page_positions[follower]:
                    return False
    return True

# Function to reorder an invalid update using topological sorting
def reorder_update(update, order):
    update_pages = update.split(",")
    # Build adjacency list and in-degree count for pages in the update
    adjacency = defaultdict(list)
    in_degree = defaultdict(int)
    
    for page in update_pages:
        adjacency[page] = []  # Initialize adjacency list
        in_degree[page] = 0   # Initialize in-degrees
    
    for page, followers in order.items():
        if page in update_pages:
            for follower in followers:
                if follower in update_pages:
                    adjacency[page].append(follower)
                    in_degree[follower] += 1

    # Perform topological sort
    queue = deque([page for page in update_pages if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in adjacency[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

# Process all updates and fix the invalid ones
invalid_middle_pages = []
for update in actuals:
    if not is_valid_order(update, order):
        corrected_order = reorder_update(update, order)
        middle_index = len(corrected_order) // 2
        invalid_middle_pages.append(int(corrected_order[middle_index]))

# Sum of middle page numbers for fixed updates
print(sum(invalid_middle_pages))
