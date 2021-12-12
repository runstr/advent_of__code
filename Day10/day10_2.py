import Tools
import os
import time
day = os.path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"

def execution():
    input_full = Tools.read_input_as_line(input_filename)
    t0 = time.time()
    all_openers = "([{<"

    point_mapping = {")": 1, "]": 2, "}": 3, ">": 4}
    mapping = {"[": "]", "{": "}", "<": ">", "(": ")"}
    line_closings = []
    line_scorings = []
    for input_line in input_full:
        line_corrupt = False
        opener = ""
        for sign in input_line:
            if sign in all_openers:
                opener += sign
            else:
                last_opener = opener[-1]
                if sign == mapping[last_opener]:
                    opener = opener[:-1]
                    continue
                else:
                    line_corrupt = True
                    break

        closers = ""
        if not line_corrupt:
            scoring = 0
            for i in range(len(opener)-1, -1, -1):
                closer = mapping[opener[i]]
                closers += closer
                scoring = scoring*5+point_mapping[closer]
            line_closings.append(closers)
            line_scorings.append(scoring)

    answer = sorted(line_scorings)[int(len(line_scorings)/2)]
    t1 = time.time()
    print("Answer to day {} task two is: {}".format(day, answer))
    print("Time of task two = {}".format(t1-t0))

