def read_full_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
    return input


def read_input_as_line(filename):
    with open(filename, 'r') as file:
        input = file.read().splitlines()
    return input
