import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"

segmnets = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

numbers = [2, 4, 3, 7]

def execution():
    input_full = Tools.read_input_as_line(input_filename)
    inputs = []
    outputs = []
    total_numbers = 0
    for input_s in input_full:
        inp, outp = input_s.split(" | ")
        outputs.append(outp.split(" "))
        inputs.append(inp.split(" "))

    for outp in outputs:
        for number in outp:
            if len(number) in numbers:
                total_numbers += 1

    print("Answer to day 8 task one is: {}".format(total_numbers))
