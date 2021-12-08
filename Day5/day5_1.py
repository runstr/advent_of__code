import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"

def get_coordinates():
    """
    Get coordinates from input file and reformat to list of int with [x1,y1,x2,y2] format, and find max x, and y
    coordinates
    :return: input coordinates, max_x and max_y coordinates
    """
    input_full = Tools.read_input_as_line(input_filename)
    max_x, max_y = 0, 0
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
    """
    From coordinate add line to map
    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :param full_map: map with lines
    :return: Nothing
    """
    diffx = abs(x2-x1)
    diffy = abs(y2-y1)

    #Calculate dx and dy that will be used to add points to the map
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

    # Add dots to map
    for i in range(0, diff + 1):
        full_map[y1+dy*i][x1+dx*i] += 1
    pass

def check_map(full_map):
    """
    Fin number of values in map larger than 1
    :param full_map:
    :return:
    """
    sum1 = sum([i.count(1) for i in full_map])
    sum0 = sum([i.count(0) for i in full_map])
    total_size = len(full_map)*len(full_map[0])
    return total_size-sum1-sum0

def execution():
    all_lines, max_x, max_y = get_coordinates()
    full_map = [[0]*(max_x+1) for _ in range(0, max_y+1)] #instansiate map with dots
    for coordinates in all_lines:
        x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
        if x1 == x2 or y1 == y2:
            add_line_to_map(x1, x2, y1, y2, full_map)
    answer = check_map(full_map)
    print("Answer to day {} task one is: {}".format(day, answer))


