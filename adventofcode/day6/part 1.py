def track_guard_path(grid):
    # Find starting position and direction
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in "^v<>":
                start_row, start_col = row, col
                direction = grid[row][col]
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
    
    visited = set([(start_row, start_col)])
    current_row, current_col = start_row, start_col
    
    while True:
        # Try to move forward
        dr, dc = directions[direction]
        next_row, next_col = current_row + dr, current_col + dc
        
        # Check if next position is out of bounds or blocked
        if (next_row < 0 or next_row >= len(grid) or 
            next_col < 0 or next_col >= len(grid[0]) or 
            grid[next_row][next_col] == '#'):
            # Turn right
            direction = turn_right[direction]
            continue
        
        # Move forward
        current_row, current_col = next_row, next_col
        visited.add((current_row, current_col))
        
        # Check if we've left the map
        if (current_row == 0 or current_row == len(grid) - 1 or 
            current_col == 0 or current_col == len(grid[0]) - 1):
            break
    
    return len(visited)

# Read the input
with open("C:\\Users\\garba\\Downloads\\adventcode.csv", "r") as file:
    grid = [line.strip() for line in file]

print(track_guard_path(grid))