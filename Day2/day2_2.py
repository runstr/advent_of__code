import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    #input_full = list(map(int, Tools.read_input_as_line(input_filename)))
    input_full = Tools.read_input_as_line(input_filename)
    direction = []
    stepsize = []
    for i in input_full:
        dir, step = i.split(" ")
        direction.append(dir)
        stepsize.append(int(step))

    horizontal = 0
    depth = 0
    aim = 0
    for i in range(0, len(direction)):
        if direction[i] == "down":
            aim += stepsize[i]
        if direction[i] == "up":
            aim -= stepsize[i]
        if direction[i] == "forward":
            horizontal += stepsize[i]
            depth += aim*stepsize[i]
    print("Answer to day {} task one is: {}".format(day, horizontal*depth))

