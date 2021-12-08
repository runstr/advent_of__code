import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = list(map(int, Tools.read_input_as_line(input_filename)[0].split(",")))
    fuel_dict = {}
    for i in range(0, max(input_full)):
        fuel = 0
        for position in input_full:
            fuel+=sum(range(abs(position-i)+1))

        fuel_dict[i]=fuel
    min(list(fuel_dict.values()))
    answer = min(list(fuel_dict.values()))

    print(fuel_dict)

    print("Answer to day7 task one is: {}".format(answer))

