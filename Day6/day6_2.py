import Tools
import os
advent_day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = list(map(int, Tools.read_input_as_line(input_filename)[0].split(",")))
    states = [0]*10
    for i in input_full:
        states[i] += 1
    number_of_days = 265
    for day in range(1, number_of_days):
        for i in range(0, 9):
            states[i] = states[i+1]
        states[9] = states[0]
        states[7] += states[0]
        states[0] = 0
    fish = sum(states)
    print("Answer to day {} task one is: {}".format(advent_day, fish))

