import Tools
import os
import time
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = Tools.read_input_as_line(input_filename)
    t_before = time.time()
    risk_level = 0
    low_point = []
    for j in range(0, len(input_full)):
        for i in range(0, len(input_full[0])):
            low_point_bool = True
            for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                try:
                    if j + dy < 0 or j + dx < 0:
                        continue
                    if int(input_full[j][i]) >= int(input_full[j + dy][i + dx]):
                        low_point_bool = False
                    else:
                        continue
                except IndexError:
                    continue
            if low_point_bool:
                low_point.append([j, i])
                risk_level += (int(int(input_full[j][i])) + 1)
    t_after = time.time()
    print("Answer to day {} task one is: {}".format(day, risk_level))
    print("Time of code 1 =  {}".format(t_after-t_before))