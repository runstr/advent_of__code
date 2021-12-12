from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"

def increase_values(octopuses):
    flashing=True
    while(flashing):
        flashing = False
        for y in range(0,len(octopuses)):
            for x in range(0, len(octopuses[0])):
                if octopuses[y][x] >9:
                    octopuses[y][x]=-1
                    flashing=True
                    for dx, dy in [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                        try:
                            if x+dx <0 or y+dy<0:
                                continue
                            if octopuses[y+dy][x+dx] != -1:
                                octopuses[y+dy][x+dx]+=1
                        except IndexError:
                            continue


def flash(octopuses):
    flashes = 0
    for y in range(0, len(octopuses)):
        for x in range(0, len(octopuses[0])):
            if octopuses[y][x] == -1:
                flashes+=1
                octopuses[y][x] =0
    return flashes


def execution():
    input_full = read_input_as_line(input_filename)
    octopuses = []
    for inp in input_full:
        octopuses.append([int(i) for i in inp])
    octopuses = np.array(octopuses)
    step=0
    while step<10000:
        octopuses+=1
        increase_values(octopuses)
        todays_flashes = flash(octopuses)
        if todays_flashes == 100:
            answer = step+1
            break
        step+=1
    print("Answer to day {} task one is: {}".format(day, answer))
