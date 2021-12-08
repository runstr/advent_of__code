import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"
checkmark = "X"
def read_input_file():
    input_full = Tools.read_full_input(input_filename)
    temp = input_full.split("\n")
    numbers = list(map(int,temp[0].split(',')))
    temp.pop(0)
    temp.pop(0)
    boards = {}
    board_number = 0
    for line in temp:
        if line !="":
            temp_line = list(map(int, line.split()))
            try:
                boards[board_number].append(temp_line)
            except:
                boards[board_number] = [temp_line]
        else:
            board_number+=1
    return numbers, boards

def update_board(board, number):
    for line in board:
        for a in line:
            if a == number:
                x_index = board.index(line)
                y_index = line.index(a)
                board[x_index][y_index] = checkmark
def check_board(board):
    for i in range(0, len(board[0])):
        if board[i][0]=='X' and board[i][1]=='X' and board[i][2]=='X' and board[i][3]=='X' and board[i][4]=='X':
            return True
        if board[0][i]=='X' and board[1][i]=='X' and board[2][i]=='X' and board[3][i]=='X' and board[4][i]=='X':
            return True
    return False

def calculate_board(board, number_in):
    sum = 0
    for line in board:
        for number in line:
            if number != "X":
                sum+=number
    return sum*number_in

def execution():
    numbers, boards = read_input_file()
    boards_won = {}
    for number in numbers:
        for board_number, board in boards.items():
            if board_number in boards_won.keys():
                continue
            update_board(board, number)
            if check_board(board):
                boards_won[board_number] = calculate_board(board, number)
    print(boards_won)
    print("Answer to day {} task one is: {}".format(day, boards_won[list(boards_won.keys())[-1]]))


