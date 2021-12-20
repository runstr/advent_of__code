from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"


def execution():
    input_full = read_input_as_line(test_input1_filename)
    scanners = {0:[]}
    i=1
    scanner_number = 0
    while i != len(input_full):
        if input_full[i]=="":
            scanner_number+=1
            i+=2
            scanners[scanner_number] = []
        else:
            scanners[scanner_number].append(list(map(int, input_full[i].split(','))))
            i+=1
    for scanner in scanners:
        print(len(scanners[scanner]))
        print()


    print("Answer to day {} task one is: {}".format(day, input_full))
