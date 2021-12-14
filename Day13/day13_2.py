from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"

def instatiate_array(x_arr,y_arr):
    map = [[0 for _ in range(0,max(x_arr)+1)] for _ in range(0, max(y_arr)+1)]
    for i in range(0, len(x_arr)):
        map[y_arr[i]][x_arr[i]] = 1
    return map

def fold_map(map, fold_dir, fold_line):
    if fold_dir=="x":
        x_length = max(len(map[0])-1 - fold_line, fold_line)
        new_map = [[0 for _ in range(0, x_length)] for _ in range(0, len(map))]
        for y in range(0, len(map)):
            i=-1
            for x in range(fold_line + 1,len(map[0])):
                new_map[y][i]+= map[y][x]
                i-=1
        for y in range(0, len(map)):
            for x in range(fold_line-1, -1, -1):
                new_map[y][x-fold_line] += map[y][x]

    elif fold_dir=="y":
        y_length = max(len(map)-1-fold_line, fold_line)
        new_map = [[0 for _ in range(0, len(map[0]))] for _ in range(0, y_length)]
        i=-1
        for y in range(fold_line+1, len(map)):
            for x in range(0, len(map[0])):
                new_map[i][x]+= map[y][x]
            i-=1
        for y in range(fold_line-1, -1, -1):
            for x in range(0, len(map[0])):
                new_map[y-fold_line][x] += map[y][x]
    else:
        new_map = []
    return new_map

def count_dots(map):
    sum = 0
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if map[y][x]:
                sum += 1
    return sum

def execution():
    input_full = read_input_as_line(input_filename)
    x_arr = []
    y_arr= []
    fold = []
    for line in input_full:
        if line[0:4] == "fold":
            fold.append(line)
        else:
            x, y = line.split(',')
            x_arr.append(int(x))
            y_arr.append(int(y))
    map = instatiate_array(x_arr, y_arr)
    for foldline in fold:
        _, _, temp = foldline.split()
        direction, coordinate = temp.split("=")
        map = fold_map(map, direction, int(coordinate))
    for y in range(0, len(map)):
        line =""
        for x in range(0, len(map[0])):
            if map[y][x]>0:
                line+=" # "
            else:
                line+=" . "
        print(line)
