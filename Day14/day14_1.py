from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"


def execution():
    input_full = read_input_as_line(input_filename)
    polymer = input_full[0]
    insertions = {}
    for i in range(2, len(input_full)):
        pair, letter = input_full[i].split(" -> ")
        insertions[pair] = letter
    insertion_time = 10
    for _ in range(0, insertion_time):
        index_dict = {}
        for i in range(0, len(polymer)-1):
            polymer_pair = polymer[i] + polymer[i+1]
            try:
                letter = insertions[polymer_pair]
            except KeyError:
                continue
            index_dict[i+1] = letter
        index_dict = sorted(index_dict.items())
        index_addition = 0
        for index, letter in index_dict:
            index = index+index_addition
            polymer = polymer[:index]+letter+polymer[index:]
            index_addition += 1
    lengths = []
    for i in set(polymer):
        lengths.append(polymer.count(i))
    lengths = sorted(lengths)
    answer = lengths[-1]-lengths[0]
    print("Answer to day {} task one is: {}".format(day, answer))
