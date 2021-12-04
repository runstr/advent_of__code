import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"

def remove_number(input_list, index, letter):
    new_list = []
    for inputs in input_list:
        if inputs[index]==letter:
            new_list.append(inputs)
    return new_list
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
    oxygen_numbers = input_full
    co2_numbers=input_full
    length = len(input_full[0])
    for i in range(0, length):
        oxygen_numbers_list = convert_to_binary_numbers(oxygen_numbers)
        Co2_numbers_list =convert_to_binary_numbers(co2_numbers)
        co2_ones = Co2_numbers_list[i].count("1")
        co2_zeros = Co2_numbers_list[i].count("0")
        oxygen_ones = oxygen_numbers_list[i].count("1")
        oxygen_zeros = oxygen_numbers_list[i].count("0")
        if oxygen_ones >= oxygen_zeros:
            if len(oxygen_numbers) !=1:
                oxygen_numbers = remove_number(oxygen_numbers, i, "1")
        else:
            if len(oxygen_numbers) != 1:
                oxygen_numbers = remove_number(oxygen_numbers, i, "0")
        if co2_ones >= co2_zeros:
            if len(co2_numbers) !=1:
                co2_numbers = remove_number(co2_numbers, i, "0")
        else:
            if len(co2_numbers) != 1:
                co2_numbers = remove_number(co2_numbers, i, "1")

    answer = int(co2_numbers[0],2)*int(oxygen_numbers[0], 2)
    print("Answer to day3 task two is: {}".format(answer))


