from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"

def get_caves(input_full):
    cave_mappings = defaultdict(list)
    for caves in input_full:
        cave1, cave2 = caves.split("-")
        cave_mappings[cave1].append(cave2)
        cave_mappings[cave2].append(cave1)
    return cave_mappings

def check_path(cave, cave_mapping, paths, current_path, search):
    new_current_path = current_path.copy()
    new_current_path.append(cave)
    if cave == "end":
        paths.append(current_path)
        search[0] =False
        return

    for new_cave in cave_mapping[cave]:
        if new_cave == "start" or (new_cave.islower() and new_cave in current_path):
            continue
        else:
            check_path(new_cave, cave_mapping, paths, new_current_path, [True])
    search[0]=False
    return


@timeexecution
def execution():
    input_full = read_input_as_line(input_filename)
    cave_mapping= get_caves(input_full)
    paths = []
    for start_cave in cave_mapping["start"]:
        check_path(start_cave, cave_mapping, paths, ["start"], [True])
    print("Answer to day {} task one is: {}".format(day, len(paths)))
