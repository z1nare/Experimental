from collections import defaultdict

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
    # Convert update into integers
    update_pages = update.split(",")
    # Map each page to its index in the update for quick lookup
    page_positions = {page: idx for idx, page in enumerate(update_pages)}
    
    # Check the rules
    for page, must_follow in order.items():
        if page in page_positions:  # Only check rules if the page is in the update
            for follower in must_follow:
                if follower in page_positions and page_positions[page] > page_positions[follower]:
                    return False
    return True

# Validate each update and find the middle page for valid updates
valid_middle_pages = []
for update in actuals:
    if is_valid_order(update, order):
        update_pages = [int(x) for x in update.split(",")]
        middle_index = len(update_pages) // 2
        valid_middle_pages.append(update_pages[middle_index])

# Sum of middle page numbers
print(sum(valid_middle_pages))
