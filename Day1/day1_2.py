import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"input_input.txt"


def execution():
    input_full = list(map(int, Tools.read_input_as_line(input_filename)))
    prev_sum = input_full[0]+input_full[1]+input_full[2]
    bigger = 0
    for i in range(3, len(input_full)):
        sum_now = input_full[i-2]+input_full[i-1]+input_full[i]
        if sum_now > prev_sum:
            bigger += 1
        prev_sum = sum_now
    print("Answer to day {} task one is: {}".format(day, bigger))

