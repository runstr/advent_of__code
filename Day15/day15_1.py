from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"
max_y_length = 0
max_x_length = 0

def get_smallest_node(unvisited, vertex):
    min_num = 1e10
    new_node = None
    index = None
    for i in range(0, len(unvisited)):
        node = unvisited[i]
        if vertex[node] < min_num:
            min_num = vertex[node]
            new_node = node
            index = i
    return index, new_node


def execution():
    input_full = read_input_as_int(input_filename)
    max_y_length = len(input_full)-1
    max_x_length = len(input_full[0])-1
    # Create unvisited sets with the weighted number
    lengths = {}
    for x in range(0, len(input_full[0])):
        for y in range(0, len(input_full)):
            lengths[(x, y)] = input_full[y][x]

    vertex = {}
    unvisited_sets = list(lengths.keys())
    for coordinates in unvisited_sets:
        if coordinates == (0, 0):
            vertex[coordinates] = 0
        else:
            vertex[coordinates] = 1e9

    visited = []
    while unvisited_sets:
        index, node = get_smallest_node(unvisited_sets, vertex)
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if node[0] + dx < 0 or node[0] + dx > max_x_length or node[1] + dy < 0 or node[1] + dy > max_y_length:
                continue
            new_node = (node[0] + dx, node[1] + dy)
            if new_node in visited:
                continue
            total_distance = vertex[node] + lengths[new_node]
            if total_distance < vertex[new_node]:
                vertex[new_node] = total_distance
        unvisited_sets.pop(index)
        visited.append(node)


    print("Answer to day {} task one is: {}".format(day, vertex[max_x_length, max_y_length]))
