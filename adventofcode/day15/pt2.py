robot_r, robot_c = -1, -1
 
def would_hit_wall(cr, cc):
  for wall in walls:
    if cr == wall[0] and cc == wall[1]:
      return True
  return False
 
def try_to_move():
  global robot_r
  global robot_c
  new_r, new_c = robot_r + dr, robot_c + dc
  if would_hit_wall(new_r, new_c):
    return
  box_in_way = None
  for box in boxes:
    if new_r == box[0] and new_c - box[1] in [0, 1]:
      box_in_way = box
      break
  if box_in_way == None:
    robot_r, robot_c = new_r, new_c
    return
  boxes_can_move = True
  boxes_to_examine = [box]
  boxes_to_move = []
  while len(boxes_to_examine) > 0:
    box = boxes_to_examine[0]
    boxes_to_examine = boxes_to_examine[1:]
    if box in boxes_to_move:
      continue
    if would_hit_wall(box[0] + dr, box[1] + dc) or would_hit_wall(box[0] + dr, box[1] + dc + 1):
      boxes_can_move = False
      break
    boxes_to_move.append(box)
    for other_box in boxes:
      if other_box in boxes_to_move:
        continue
      if box[0] + dr == other_box[0] and box[1] + dc - other_box[1] in [-1, 0, 1]:
        boxes_to_examine.append(other_box)
  if boxes_can_move:
    robot_r, robot_c = new_r, new_c
    for box in boxes_to_move:
      box[0] += dr
      box[1] += dc
  return
 
walls = []
boxes = []
directions = ""
 
found_blank_line = False
r = 0
file = open("C:\\Users\\garba\\Downloads\\adventcode.csv", "r")
for line in file:
  line = line.replace("\n", "")
  if line == "":
    found_blank_line = True
    continue
  if found_blank_line:
    directions += line
    continue
  c = 0
  for character in line:
    if character == "@":
      robot_r, robot_c = r, c
    if character == "#":
      walls.append([r, c])
      walls.append([r, c + 1])
    if character == "O":
      boxes.append([r, c])
    c += 2
  r += 1
 
for character in directions:
  dr, dc = -2, -2
  if character == "^":
    dr, dc = -1, 0
  if character == "v":
    dr, dc = 1, 0
  if character == "<":
    dr, dc = 0, -1
  if character == ">":
    dr, dc = 0, 1
  if dr == -2:
    continue
  try_to_move()
 
total = 0
for box in boxes:
  total += 100 * box[0] + box[1]
print (total)