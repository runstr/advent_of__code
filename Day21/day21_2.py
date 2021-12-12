from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"


def execution():
    input_full = read_input_as_line(input_filename)

    print("Answer to day {} task two is: {}".format(day, input_full))

