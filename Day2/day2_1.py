import Tools

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
    for i in range(0, len(direction)):
        if direction[i] == "down":
            depth += stepsize[i]
        if direction[i] == "up":
            depth -= stepsize[i]
        if direction[i] == "forward":
            horizontal += stepsize[i]
        if direction[i] == "backwards":
            horizontal -= stepsize[i]
    print(horizontal*depth)