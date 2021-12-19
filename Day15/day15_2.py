import sys

from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"


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

def multiply_input(input_full, multiply):
    y_length = len(input_full)
    x_length = len(input_full[0])
    new_input = [[0 for _ in range(x_length*multiply)] for _ in range(y_length*multiply)]
    for x in range(len(input_full[0])):
        for y in range(len(input_full)):
            for i_x in range(0, multiply):
                for i_y in range(0, multiply):
                    new_value = input_full[y][x]+ i_y+ i_x
                    if new_value>9:
                        new_value = new_value-9
                    new_input[y+i_y*y_length][x+i_x*x_length] = new_value
    return new_input
def execution():
    input_full = read_input_as_int(input_filename)
    new_input = multiply_input(input_full, 5)
    max_y_length = len(new_input) - 1
    max_x_length = len(new_input[0]) - 1


    # Create unvisited sets with the weighted number
    lengths = {}
    for x in range(0, len(new_input[0])):
        for y in range(0, len(new_input)):
            lengths[(x, y)] = new_input[y][x]

    unvisited = {}
    unvisited_keys = list(lengths.keys())
    for coordinates in unvisited_keys:
        if coordinates == (0, 0):
            unvisited[coordinates] = (0, None)
        else:
            unvisited[coordinates] = (0, None)
    priority_list = [(0, 0)]
    visited = {}
    visited_keys = []
    while unvisited_keys:
        node = priority_list.pop(0)
        visited_keys.append(node)
        visited[node] = unvisited[node]
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if node[0] + dx < 0 or node[0] + dx > max_x_length or node[1] + dy < 0 or node[1] + dy > max_y_length:
                continue
            new_node = (node[0] + dx, node[1] + dy)
            if new_node in visited:
                continue
            total_distance = unvisited[node][0] + lengths[new_node]
            if total_distance < unvisited[new_node][0]:
                unvisited[new_node][0][new_node] = total_distance
            if priority_list:
                for i in priority_list:
                    unvisited[1]

        visited.append(node)

    print("Answer to day {} task two is: {}".format(day, vertex[max_x_length, max_y_length]))

