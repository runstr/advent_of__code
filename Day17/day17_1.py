from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"
distinct_velocities = []
def get_min_x(x_min):
    x=1
    while True:
        sum_x = 0
        for i in range(0, x+1):
            sum_x += x-i
        if sum_x>=x_min:
            return x
        else:
            x+=1


def get_x_values(x_start_min, x_min, x_max):
    x_values = {}
    for x_start in range(0, x_max):
        x = 0
        x_i = x_start
        while x < x_max:
            x += x_i
            if x_i==0:
                break
            if x >= x_min and x < x_max:
                try:
                    x_values[x_start].append(x)
                except:
                    x_values[x_start] = [x]
            x_i-=1
    return x_values

def get_increments(x_velocity, x_end):
    i=0
    while x_end>0:
        x_end -= x_velocity
        x_velocity -=1
        i += 1
    if x_velocity>0:
        zero_x_vel = False
    else:
        zero_x_vel = True
    return i, zero_x_vel


def get_y_values(x_velocity, x_end, y_min, y_max):
    global distinct_velocities
    increment, zero_x_vel = get_increments(x_velocity, x_end)
    y_max_velocity_end = -y_min
    print("x_velocity = ", x_velocity, ", x_end = ", x_end, ", Increment = ", increment)
    y_velocities = {}
    for y_vel in range(y_min, y_max_velocity_end):
        y=0
        if zero_x_vel:
            i = 0
            y += y_vel
            while y >= y_min:
                if y <= y_max:
                    distinct_velocities.append((x_velocity, y_vel))
                    try:
                        y_velocities[y_vel] = [y]
                    except:
                        y_velocities[y_vel].append(y)
                i += 1
                y += (y_vel - i)
        else:
            for i in range(0, increment):
                y += (y_vel-i)
            if y >= y_min and y <= y_max:
                y_velocities[y_vel] = [y]
                distinct_velocities.append((x_velocity, y_vel))

    print("y_velocities = ", y_velocities)
    pass




def execution():
    input_full = read_input_as_line(test_input1_filename)[0].strip("target area: ").split(', ')
    x_min, x_max = list(map(int, input_full[0].strip("x=").split("..")))
    y_min, y_max = list(map(int, input_full[1].strip("y=").split("..")))
    x_start_min = get_min_x(x_min)
    x_values = get_x_values(x_start_min, x_min, x_max)
    for key, values in x_values.items():
        for value in values:
            get_y_values(key, value, y_min, y_max)

    print(set(distinct_velocities))
    print(len(set(distinct_velocities)))
    print("Answer to day {} task one is: {}".format(day, 2))
