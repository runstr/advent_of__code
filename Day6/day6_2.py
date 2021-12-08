import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = list(map(int, Tools.read_input_as_line(input_filename)[0].split(",")))
    states = {}
    for i in range(0, 10):
        states[i]=0
    for i in input_full:
        states[i] += 1
    print(states)
    number_of_days = 256
    for day in range(1, number_of_days):
        for i in range(0, 9):
            states[i] = states[i+1]
        states[9] = states[0]
        states[7] += states[0]
        states[0] = 0
    print(states)
    fish = 0
    for k, v in states.items():
        fish+=v


    print("Answer to day1 task two is: {}".format(fish))

