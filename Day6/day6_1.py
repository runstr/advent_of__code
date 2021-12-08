import Tools
import time
from matplotlib import pyplot as plt

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = list(map(int, Tools.read_input_as_line(input_filename)[0].split(",")))
    states=input_full
    number_of_days = 256
    new_fish=0
    days = []
    time_taken = []
    for day in range(0, number_of_days):
        time_before = time.time()
        states += [9]*new_fish
        new_fish = 0
        for i in range(0, len(states)):
            states[i]-=1
            if states[i] ==0:
                new_fish+=1
                states[i] = 7
        time_after = time.time()
        days.append(day)
        time_taken.append(time_after-time_before)
        plt.plot(days, time_taken)
        plt.pause(0.05)
        plt.clf()
        print("Day {} took {} s to run".format(day, time_after-time_before))

    answer = len(states)

    #print(states)
    print("Answer to day6 task one is: {}".format(answer))
