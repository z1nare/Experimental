def track_guard_path_with_obstacle(grid, new_obstacle_position):
    # Create a copy of the grid with the new obstacle placed
    grid_copy = [list(row) for row in grid]
    row, col = new_obstacle_position
    grid_copy[row][col] = '#'

    # Find the starting position and direction
    for row in range(len(grid_copy)):
        for col in range(len(grid_copy[row])):
            if grid_copy[row][col] in "^v<>":
                start_row, start_col = row, col
                direction = grid_copy[row][col]
                break
        else:
            continue
        break
    
    # Directions: Up, Right, Down, Left
    directions = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    
    # Turning right mapping
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    visited = set([(start_row, start_col, direction)])
    current_row, current_col = start_row, start_col
    
    while True:
        # Try to move forward
        dr, dc = directions[direction]
        next_row, next_col = current_row + dr, current_col + dc
        
        # Check if next position is out of bounds or blocked
        if (next_row < 0 or next_row >= len(grid_copy) or 
            next_col < 0 or next_col >= len(grid_copy[0]) or 
            grid_copy[next_row][next_col] == '#'):
            # Turn right
            direction = turn_right[direction]
            continue
        
        # Move forward
        current_row, current_col = next_row, next_col
        if (current_row, current_col, direction) in visited:
            return True  # Loop detected
        
        visited.add((current_row, current_col, direction))
        
        # Check if we've left the map
        if (current_row == 0 or current_row == len(grid_copy) - 1 or 
            current_col == 0 or current_col == len(grid_copy[0]) - 1):
            break
    
    return False

def find_all_possible_obstacles(grid):
    # Track all positions that could cause the guard to get stuck in a loop
    possible_positions = 0
    
    for row in range(1, len(grid) - 1):  # Start from row 1 to avoid boundary errors
        for col in range(1, len(grid[row]) - 1):  # Start from col 1 for the same reason
            if grid[row][col] == '.':  # Only empty spaces are valid positions for new obstacles
                if track_guard_path_with_obstacle(grid, (row, col)):  # Check if adding an obstacle here causes a loop
                    possible_positions += 1
    
    return possible_positions

# Read the input
with open("C:\\Users\\garba\\Downloads\\adventcode.csv", "r") as file:
    grid = [line.strip() for line in file]

# Find the number of positions where adding an obstruction will cause the guard to get stuck in a loop
print(find_all_possible_obstacles(grid))
