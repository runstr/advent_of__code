import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"input_input.txt"


def execution():
    input_full = Tools.read_input_as_line(input_filename)


    print("Answer to day {} task one is: {}".format(day, input_full))

