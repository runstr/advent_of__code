import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = Tools.read_input_as_line(input_filename)
    bigger=0
    prev = 1000000000
    for i in input_full:
        if i > prev:
            bigger += 1
        prev = i
    print("Answer to day1 task one is: {}".format(bigger))
