import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"

def get_coordinates():
    input_full = Tools.read_input_as_line(input_filename)
    max_x, max_y = 0,0
    for i in range(0, len(input_full)):
        x1, y1, x2, y2 = list(map(int, input_full[i].replace(" -> ", ',').split(',')))
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
        input_full[i] = [x1, y1, x2, y2]
    return input_full, max_x, max_y


def add_line_to_map(x1, x2, y1, y2, full_map):
    diffx = abs(x2-x1)
    diffy = abs(y2-y1)
    if diffx:
        diff = diffx
        dx = (x2 - x1) // diffx
        if diffy:
            dy = (y2 - y1) // diffy
        else:
            dy = 0
    else:
        diff = diffy
        dx = 0
        dy = (y2 - y1) // diffy

    for i in range(0, diff + 1):
        try:
            full_map[y1+dy*i][x1+dx*i] += 1
        except TypeError:
            full_map[y1+dy*i][x1+dx*i] = 1
    pass

def check_map(full_map):
    overlaps  = 0
    for line in full_map:
        for point in line:
            if point != '.':
                if point>=2:
                    overlaps += 1
    return overlaps

def execution():
    all_lines, max_x, max_y = get_coordinates()
    full_map = [['.']*(max_x+1) for _ in range(0, max_y+1)]
    for coordinates in all_lines:
        x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
        add_line_to_map(x1, x2, y1, y2, full_map)
    answer = check_map(full_map)
    #for line in full_map:
    #    print(line)
    print("Answer to day2 task two is: {}".format(answer))


