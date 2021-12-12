import Tools
import os
import time
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def part1(input_full, rows, columns):
    risk_level = 0
    low_point = []
    for j in range(0, rows):
        for i in range(0, columns):
            low_point_bool = True
            for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                try:
                    if j + dy < 0 or j+dx<0:
                        continue
                    if input_full[j][i] >= input_full[j+dy][i+dx]:
                        low_point_bool = False
                    else:
                        continue
                except IndexError:
                    continue
            if low_point_bool:
                low_point.append([j,i])
                risk_level += input_full[j][i] + 1

    return low_point

def find_basins(input_full, point, basin_points, rows, columns):
    if input_full[point[0]][point[1]] != 9:
        basin_points.append(point)
    else:
        return
    for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        if point[0]+dy < 0 or point[1]+dx < 0 or point[0]+dy >= rows or point[1]+dx >= columns:
            continue
        try:
            if input_full[point[0]][point[1]] < input_full[point[0]+dy][point[1]+dx]:
                find_basins(input_full, [point[0]+dy, point[1]+dx], basin_points, rows, columns)
        except:
            continue

def unique_parts(basins):
    unique_basins = []
    for basin in basins:
        if basin not in unique_basins:
            unique_basins.append(basin)
    return unique_basins


def execution():
    time_before = time.time()
    input_full = Tools.read_input_as_line(input_filename)
    for i in range(0, len(input_full)):
        input_full[i] = list(map(int, input_full[i]))
    rows = len(input_full)
    columns = len(input_full[0])
    low_points = part1(input_full, rows, columns)
    basins = {}
    basins_length = {}
    for low_point in low_points:
        basins_points = [low_point]
        find_basins(input_full, low_point, basins_points, rows, columns)
        unique_basins = unique_parts(basins_points)
        basins[str(low_point[0])+","+str(low_point[1])] =unique_parts(basins_points)
        basins_length[str(low_point[0])+","+str(low_point[1])] = len(unique_basins)
    sorted_basin_lengths = sorted(list(basins_length.values()))
    time_after = time.time()

    print("Answer to day {} task one is: {}".format(day, sorted_basin_lengths[-1]*sorted_basin_lengths[-2]*sorted_basin_lengths[-3]))
    print("Time of code 2 =  {}".format(time_after-time_before))
