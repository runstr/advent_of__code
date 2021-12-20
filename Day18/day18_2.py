from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"

def calculate_number(full_number):
    while full_number[0]=="[":
        i=0
        while i < len(full_number):
            if full_number[i].isdigit():
                found_number = False
                start_index = i-1
                left_number=""
                while True:
                    if full_number[i].isdigit():
                        left_number += full_number[i]
                        i+=1
                    elif full_number[i]=="," and full_number[i+1].isdigit():
                        found_number = True
                        i+=1
                        right_number = full_number[i]
                        i+=1
                        while full_number[i].isdigit():
                            right_number += full_number[i]
                            i+=1
                        end_index = i
                        break
                    else:
                        break
                if found_number:
                    new_number = str(int(left_number)*3 + int(right_number)*2)
                    full_number = full_number[:start_index]+new_number+full_number[end_index+1:]
                    i=start_index+len(new_number)+1
            i+=1
    return full_number

def split_number(index, snail_number, number):
    left_number = str(int(number) // 2)
    right_number = str(int(number) // 2 + int(number) % 2)
    snail_number = snail_number[:index]+"["+left_number+","+right_number+"]"+snail_number[index+len(number):]
    return snail_number

def explode_number(index, snail_number):
    i = index+1
    left_number = snail_number[i]
    i+=1
    while snail_number[i].isdigit():
        left_number += snail_number[i]
        i += 1
    i += 1
    right_number = snail_number[i]
    i += 1
    while snail_number[i].isdigit():
        right_number += snail_number[i]
        i += 1
    snail_number = snail_number[:index] + "0" + snail_number[i+1:]
    new_number = "0"
    for end_index in range(index-1, -1, -1):
        if snail_number[end_index].isdigit():
            new_number = snail_number[end_index]
            start_index = end_index-1
            while snail_number[start_index].isdigit():
                new_number = snail_number[start_index] + new_number
                start_index-=1
            new_number = str(int(new_number)+int(left_number))
            snail_number = snail_number[:start_index+1]+new_number+snail_number[end_index+1:]
            break
    for start_index in range(index+len(new_number), len(snail_number)):
        if snail_number[start_index].isdigit():
            new_number = snail_number[start_index]
            end_index = start_index + 1
            while snail_number[end_index].isdigit():
                new_number += snail_number[end_index]
                end_index += 1
            new_number = str(int(new_number) + int(right_number))
            snail_number = snail_number[:start_index] + new_number + snail_number[end_index:]
            break

    return snail_number

def add_numbers(leftside, rightside):
        snail_number = "["+leftside+","+ rightside+"]"
        while True:
            exploded = False
            opening_brackets = 0
            for index in range(0, len(snail_number)):
                if snail_number[index] == "[":
                    opening_brackets += 1
                elif snail_number[index] == "]":
                    opening_brackets -= 1
                if opening_brackets == 5:
                    snail_number = explode_number(index, snail_number)
                    exploded=True
                    break
            spliced = False
            if not exploded:
                for index in range(0, len(snail_number)):
                    if snail_number[index].isdigit() and snail_number[index+1].isdigit():
                        number = snail_number[index]
                        i=index+1
                        while snail_number[i].isdigit():
                            number += snail_number[i]
                            i += 1
                        snail_number = split_number(index, snail_number, number)
                        spliced = True
                        break
            if not exploded and not spliced:
                break

        return calculate_number(snail_number)

def execution():
    input_full = read_input_as_line(input_filename)
    calculated_numbers = []
    for leftside_index in range(0, len(input_full)-1):
        for rightside_index in range(leftside_index+1, len(input_full)):
            calculated_numbers.append(int(add_numbers(input_full[leftside_index], input_full[rightside_index])))
            calculated_numbers.append(int(add_numbers(input_full[rightside_index], input_full[leftside_index])))
    print("Answer to day {} task two is: {}".format(day, max(calculated_numbers)))