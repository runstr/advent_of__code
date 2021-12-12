from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"

def execution():
    input_full = read_input_as_line(input_filename)
    t0 = time()
    all_openers = "([{<"

    mapping = {"[": "]", "{": "}", "<": ">", "(": ")"}

    line_corrupters = []
    for input_line in input_full:
        opener = ""
        for sign in input_line:
            if sign in all_openers:
                opener+=sign
            else:
                last_opener = opener[-1]
                if sign == mapping[last_opener]:
                    opener = opener[:-1]
                    continue
                else:
                    line_corrupters.append(sign)
                    break
    point_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}
    answer = 0
    all_closers = ")]}>"
    for closer in all_closers:
        answer += line_corrupters.count(closer)*point_mapping[closer]
    t1 = time()
    print("Answer to day {} task one is: {}".format(day, answer))
    print("Time of task one = {}".format(t1 - t0))