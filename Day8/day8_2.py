import Tools

input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"
numbers_mapping = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6:  "", 7: "", 8: "", 9: ""}
letter_mapping = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6:  "", 7: ""}

def map_number(inputs, letters, number_to_decode, mapping_to_find, number_length):
    for number in inputs:
        if len(number) == number_length:
            numbers_mapping[number_to_decode] = number
            letter = numbers_mapping[number_to_decode]
            found_number = True
            for i in letters:
                if i not in number:
                    found_number = False
                    break
                letter = letter.replace(i, "")
            if found_number:
                if len(letter) == 1:
                    letter_mapping[mapping_to_find] = letter
                    break
                elif len(letter) == 0:
                    break
                else:
                    continue

def find_mapping(inputs):
    for number in inputs:
        if len(number) == 2:
            numbers_mapping[1] = number
        elif len(number) == 4:
            numbers_mapping[4] = number
        elif len(number) == 3:
            numbers_mapping[7] = number
        elif len(number) == 7:
            numbers_mapping[8] = number

    letter_mapping[0] = numbers_mapping[7].replace(numbers_mapping[1][0], "").replace(numbers_mapping[1][1], "")
    map_number(inputs, numbers_mapping[4] + letter_mapping[0], 9, 6, 6)

    map_number(inputs, numbers_mapping[1] + letter_mapping[0] + letter_mapping[6], 3, 3, 5)

    letter = numbers_mapping[9]
    for i in numbers_mapping[1] + letter_mapping[0]+letter_mapping[6]+letter_mapping[3]:
        letter = letter.replace(i, "")
    letter_mapping[1] = letter

    letter = numbers_mapping[8]
    for i in numbers_mapping[1] + letter_mapping[0]+letter_mapping[6]+letter_mapping[3]+letter_mapping[1]:
        letter = letter.replace(i, "")
    letter_mapping[4] = letter

    map_number(inputs, letter_mapping[0]+letter_mapping[1]+letter_mapping[3]+ letter_mapping[4]+letter_mapping[6], 6, 5, 6)
    letter_mapping[2] = numbers_mapping[1].replace(letter_mapping[5], "")
    map_number(inputs, letter_mapping[0]+letter_mapping[2]+letter_mapping[3]+ letter_mapping[4]+letter_mapping[6], 2, -1, 5)
    map_number(inputs, letter_mapping[0]+letter_mapping[1]+letter_mapping[2]+ letter_mapping[4]+letter_mapping[5]+letter_mapping[6], 0, -1, 6)
    map_number(inputs, letter_mapping[0]+letter_mapping[1]+letter_mapping[3]+letter_mapping[5]+letter_mapping[6], 5, -1, 5)

def find_number(numbers_mapped, outputs):
    string_number = ""
    for output in outputs:
        for number, string in numbers_mapped.items():
            if len(string)!= len(output):
                continue
            if sorted(output)==sorted(string):
                string_number+=str(number)
                break
    return int(string_number)

def execution():
    input_full = Tools.read_input_as_line(input_filename)
    inputs = []
    outputs = []
    numbers = []
    for input_s in input_full:
        inp, outp = input_s.split(" | ")
        outputs.append(outp.split(" "))
        inputs.append(inp.split(" "))
    for i in range(0, len(inputs)):
        find_mapping(inputs[i])
        numbers.append(find_number(numbers_mapping, outputs[i]))

    print("Answer to day 8 task two is: {}".format(sum(numbers)))