from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"


def execution():
    # Read input of file as lines
    input_full = read_input_as_line(input_filename)

    # Get first line for polymer string and then pair->letter translations to dict
    polymer = input_full[0]
    insertions = {}
    for i in range(2, len(input_full)):
        pair, letter = input_full[i].split(" -> ")
        insertions[pair] = letter


    # Count all letters in polymer for starting point
    letter_count = {}
    for i in polymer:
        try:
            letter_count[i] += 1
        except KeyError:
            letter_count[i] = 1

    # Create dictionary of pairs, with pair as key and number of occurences as value
    polymer_dict = {}
    for i in range(0, len(polymer)-1):
        polymer_pair = polymer[i] + polymer[i + 1]
        try:
            polymer_dict[polymer_pair] += 1
        except KeyError:
            polymer_dict[polymer_pair] = 1

    # Run x number of insertions
    insertion_time = 40
    for _ in range(insertion_time):
        # Use temporary dict for storing new poly,ers
        temp_polymer_dict = polymer_dict.copy()
        for basepair, letter in insertions.items():
            # Get occurences of specific pair in polymer, and substract number of occurences of
            # origonal polymer string in new string
            try:
                occurrences = polymer_dict[basepair]
                temp_polymer_dict[basepair] -= occurrences
            except KeyError:
                continue
            # add occurrences of that pair to count if letters that pair corresponds to
            try:
                letter_count[letter] += occurrences
            except KeyError:
                letter_count[letter] = occurrences

            # Add occurrences of new pairs equal to number of occurrences of base pair
            new_pair1 = basepair[0]+letter
            new_pair2 = letter+basepair[1]
            try:
                temp_polymer_dict[new_pair1] += occurrences
            except KeyError:
                temp_polymer_dict[new_pair1] = occurrences
            try:
                temp_polymer_dict[new_pair2] += occurrences
            except KeyError:
                temp_polymer_dict[new_pair2] = occurrences
        # Set polymer dict to be the new dict after all new occurrences has been counted
        polymer_dict = temp_polymer_dict

    answer = max(letter_count.values()) - min(letter_count.values())

    print("Answer to day {} task two is: {}".format(day, answer))
