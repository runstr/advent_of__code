import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = Tools.read_input_as_line(input_filename)
    input_full[4]
    print(len(input_full))
    print(len(input_full[0]))
    risk_level = 0
    corners = 0
    low_point = []
    for j in range(0, len(input_full)):
        for i in range(0, len(input_full[0])):
            if j==0: 
                if i==0:
                    if int(input_full[0][0])<int(input_full[1][0]) and int(input_full[0][0])<int(input_full[0][1]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)
                elif i == len(input_full[0])-1:
                    if int(input_full[0][i])<int(input_full[1][i]) and int(input_full[0][i])<int(input_full[0][i-1]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)
                else:
                    if int(input_full[0][i])<int(input_full[0][i-1]) and int(input_full[0][i])<int(input_full[0][i+1]) and int(input_full[0][i])<int(input_full[1][i]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)

            elif i == 0:
                if j == len(input_full)-1:
                    if int(input_full[j][0])<int(input_full[j-1][0]) and int(input_full[j][0])<int(input_full[j][1]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)
                else:
                    if int(input_full[j][0])<int(input_full[j-1][0]) and int(input_full[j][0])<int(input_full[j+1][0]) and int(input_full[j][0])<int(input_full[j][1]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)


            elif i == len(input_full[0])-1:
                if j == len(input_full)-1:
                    if int(input_full[j][i])<int(input_full[j-1][i]) and int(input_full[j][i])<int(input_full[j][i-1]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)
                else:
                    if int(input_full[j][i])<int(input_full[j-1][i]) and int(input_full[j][i])<int(input_full[j+1][i]) and int(input_full[j][i])<int(input_full[j][i-1]):
                        low_point.append([j, i])
                        risk_level+=(int(int(input_full[j][i]))+1)


            elif j == len(input_full)-1:
                if int(input_full[j][i])<int(input_full[j][i-1]) and int(input_full[j][i])<int(input_full[j][i+1]) and int(input_full[j][i])<int(input_full[j-1][i]):
                    low_point.append([j, i])
                    risk_level+=(int(int(input_full[j][i]))+1)


            else:
                try:
                    if (int(input_full[j][i])<int(input_full[j-1][i]) and int(input_full[j][i])<int(input_full[j+1][i]) and
                        int(input_full[j][i])<int(input_full[j][i-1]) and int(input_full[j][i])<int(input_full[j][i+1])):
                        low_point.append([j,i])
                        risk_level += (int(int(input_full[j][i])) + 1)
                except IndexError as e:
                    print(j, "  " , i)
                    raise e
    print(low_point)
    print("Answer to day {} task one is: {}".format(day, risk_level))
