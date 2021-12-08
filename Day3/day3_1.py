import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"
def convert_to_binary_numbers(input_full):
    numbers = {}
    for line in input_full:
        for i in range(0, len(line)):
            try:
                numbers[i] += line[i]
            except KeyError:
                numbers[i]=line[i]
    return numbers

def execution():
    input_full = Tools.read_input_as_line(input_filename)
    numbers = convert_to_binary_numbers(input_full)
    gamma = ""
    epsilon = ""
    for key, line in numbers.items():
        ones = line.count("1")
        zeros = line.count("0")
        if ones>zeros:
            gamma+="1"
            epsilon+="0"
        else:
            gamma+="0"
            epsilon+="1"
    answer = int(gamma,2)*int(epsilon,2)
    print("Answer to day {} task one is: {}".format(day, answer))
