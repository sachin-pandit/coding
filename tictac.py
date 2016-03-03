#!/usr/bin/python2.7 -tt

import sys
import copy

sneak = 0
raid = 1
task_number = -1
player1 = ""
player2 = ""
player1_battle = ""
player2_battle = ""
player1_algo = -1
player2_algo = -1
cutoff_depth = -1
depth_player1 = -1
depth_player2 = -1
cutoff_depth = -1
grid_value = [[0 for x in range(5)] for x in range(5)]
cur_board = [["" for x in range(5)] for x in range(5)]
my_total = 0
his_total = 0
temp_my_total = 0
temp_his_total = 0
attack_type = 0
star_count = 0
traverse_file = -1
battle_file = -1

def get_list(cur_board, list):
    temp = ""
    for i in range (0, 5):
        for j in range (0, 5):
            if (cur_board[i][j] == "*"):
                temp = str(i) + str(j)
                list.append (temp)
                '''
    for i in list:
        print ("%s " % (i)),
        '''

def conquer_pawn (cur_board, i, j, player1, player2):
    global his_total
    global my_total
    if ((j - 1) >= 0 and cur_board[i][j-1] == player2):
        cur_board[i][j-1] = player1
        my_total = my_total + grid_value[i][j-1]
        his_total = his_total - grid_value[i][j-1]
    if ((i - 1) >= 0 and cur_board[i-1][j] == player2):
        cur_board[i-1][j] = player1
        my_total = my_total + grid_value[i-1][j]
        his_total = his_total - grid_value[i-1][j]
    if ((j + 1) <= 4 and cur_board[i][j+1] == player2):
        cur_board[i][j+1] = player1
        my_total = my_total + grid_value[i][j+1]
        his_total = his_total - grid_value[i][j+1]
    if ((i + 1) <= 4 and cur_board[i+1][j] == player2):
        cur_board[i+1][j] = player1
        my_total = my_total + grid_value[i+1][j]
        his_total = his_total - grid_value[i+1][j]

def get_type (i, j, player, cur_board):
    if ((j - 1) >= 0 and cur_board[i][j-1] == player):
        return 1
    if ((i - 1) >= 0 and cur_board[i-1][j] == player):
        return 1
    if ((j + 1) <= 4 and cur_board[i][j+1] == player):
        return 1
    if ((i + 1) <= 4 and cur_board[i+1][j] == player):
        return 1


def get_neighbour_value (i, j):
    global attack_type
    value = 0
    if (get_type (i, j, player1, cur_board) == 1):
        attack_type = raid
        if ((j - 1) >= 0 and cur_board[i][j-1] == player2):
            value = value + grid_value[i][j-1]
        if ((i - 1) >= 0 and cur_board[i-1][j] == player2):
            value = value + grid_value[i-1][j]
        if ((j + 1) <= 4 and cur_board[i][j+1] == player2):
            value = value + grid_value[i][j+1]
        if ((i + 1) <= 4 and cur_board[i+1][j] == player2):
            value = value + grid_value[i+1][j]
        return value
    else:
        return value


def get_cell_value (index_str):
    global temp_my_total
    global temp_his_total

    index = int(index_str)
    i = index/10
    j = index%10
    temp_my_total = my_total + grid_value[i][j];
    temp_his_total = his_total
    temp = get_neighbour_value (i, j)
    if (temp > 0):
        temp_my_total = temp_my_total + temp
        temp_his_total = temp_his_total - temp

   # print ("i = %d, j = %d, myval = %d, hisval = %d, tempmyval = %d, temphisval = %d" % (i, j, my_total, his_total, temp_my_total, temp_his_total))
    return (temp_my_total - temp_his_total)

def get_eval_value (cur_board):
    xvalue = 0
    ovalue = 0

    for i in range(0, 5):
        for j in range(0, 5):
            if (cur_board[i][j] == player1):
                xvalue += grid_value[i][j]
            elif (cur_board[i][j] == player2):
                ovalue += grid_value[i][j]

    return (xvalue - ovalue)


def get_max_cell (list, max_row, max_column, final_attack_type):
    global attack_type
    max_value = -1
    temp = -1
    number = 0

    for index in list:
        attack_type = sneak
        temp = get_cell_value (index)
        if (temp > max_value or max_value == -1):
            max_value = temp
            max_row = int(index)/10
            max_column = int(index)%10
            final_attack_type = attack_type
    return (max_row, max_column, final_attack_type)

def get_min_cell (list, max_row, max_column, final_attack_type):
    global attack_type
    max_value = -1
    temp = -1
    number = 0

    for index in list:
        attack_type = sneak
        temp = get_cell_value (index)
        if (temp < max_value or max_value == -1):
            max_value = temp
            max_row = int(index)/10
            max_column = int(index)%10
            final_attack_type = attack_type
    return (max_row, max_column, final_attack_type)

def print_next_move (max_row, max_column):
    return ((chr(max_column+65) + str(max_row+1)))

def print_next_move_i (index):
    max_row = int (index) / 10
    max_column = int (index) % 10
    return ((chr(max_column+65) + str(max_row+1)))

def update_entries (max_row, max_column, final_attack_type):
    global cur_board
    global my_total
    global attack_type

    my_total = my_total + grid_value[max_row][max_column]
    cur_board[max_row][max_column] = player1
    #print ("\nFInal attack = %d" % (final_attack_type)),
    if (final_attack_type == raid):
        conquer_pawn (cur_board, max_row, max_column, player1, player2)
        attack_type = sneak
    #print("\nNext move %s" % (print_next_move (max_row, max_column))),
    #print_board_matrix (cur_board)

def print_list (list):
    for i in list:
        print ("%s" % i),
    print ("")


def print_to_battle_file(board):
    global battle_file
    try:
        battle_file = open ("trace_state.txt", "a")
        for i in range (0, 5):
            for j in range (0, 5):
                battle_file.write (board[i][j]),
            battle_file.write("\n")

    except FileNotFoundError:
        print ("File does not exist")


def open_battle_file ():
    global battle_file
    try:
        battle_file = open ("trace_state.txt", "w")

    except FileNotFoundError:
        print ("File does not exist")


def print_to_file (board):
    global task_number
    try:
        fd = open ("next_state.txt", "w")
        for i in range (0, 5):
            for j in range (0, 5):
                fd.write (board[i][j]),
            fd.write("\n")

    except FileNotFoundError:
        print ("File does not exist")

def best_first ():
    max_row = -1
    max_column = -1
    final_attack_type = sneak
    list = []

    get_list (cur_board, list)
    if (len(list) == 0):
        return

    (max_row, max_column, final_attack_type) = get_max_cell (list, max_row, max_column, final_attack_type)
    update_entries (max_row, max_column, final_attack_type)
    #print ("Final move: %s" % (print_next_move (max_row, max_column)))
    #print_board_matrix (cur_board)
    if (task_number != 4):
        print_to_file (cur_board)
    else:
        print_to_battle_file (cur_board)

def print_grid_matrix (ref_matrix):
    print ("")
    for i in range (0, 5):
        for j in range (0, 5):
            print ("%d " % ref_matrix[i][j]),
        print ("")

def print_board_matrix (cur_board):
    print ("")
    for i in range (0, 5):
        for j in range (0, 5):
            print ("%s " % cur_board[i][j]),
        print ("")

def print_value (task_number, cutoff_depth, grid_value, cur_board):
    print ("Task number = %d" % task_number)
    print ("Player1 = %s" % player1)
    print ("Player2 = %s" % player2)
    print ("cutoff_depth = %d" % cutoff_depth)
    print_grid_matrix (grid_value)
    print_board_matrix (cur_board)
    print ("My total = %d" % my_total)
    print ("His total = %d" % his_total)


def fill_char_list (line, row):
    global cur_board
    global my_total
    global his_total
    global star_count
    column = 0
    for i in range(0,5):
        cur_board[row][column] = line[column].strip()
        if (cur_board[row][column] == player1):
            my_total = my_total + grid_value[row][column]
        elif (cur_board[row][column] == player2):
            his_total = his_total + grid_value[row][column]
        else:
            star_count += 1
        column = column + 1

def fill_int_list (line, row):
    global grid_value
    column = 0
    for word in line.rstrip("\r").split():
        grid_value[row][column] = (int(word))
        column = column + 1


def process_the_file(filename):
    global task_number
    global player1
    global player2
    global cutoff_depth
    try:
        fd = open (filename, "r")
        count = 0
        for line in fd:
            if (count == 0):
                task_number = int (line)
            elif (count == 1):
                player1 = line
                player1 = player1.strip("\n").strip()
                if (player1 == "X"):
                    player2 = "O"
                else:
                    player2 = "X"
            elif (count == 2):
                cutoff_depth = int (line)
            elif (count >= 3 and count < 8):
                fill_int_list (line, count-3)
            elif (count >= 8 and count < 13):
                fill_char_list (line, count-8)
            count = count + 1

    except FileNotFoundError:
        print ("Entered file not found\n")


def process_game_file(filename):
    global player1_battle
    global player2_battle
    global player1_algo
    global player2_algo
    global depth_player1
    global depth_player2
    global task_number

    try:
        fd = open (filename, "r")
        count = 0
        for line in fd:
            if (count == 0):
                task_number = int (line)
            elif (count == 1):
                player1_battle = line
                player1_battle = player1_battle.strip("\n").strip()
            elif (count == 2):
                player1_algo = int (line)
            elif (count == 3):
                depth_player1 = int (line)
            elif (count == 4):
                player2_battle = line
                player2_battle = player2_battle.strip("\n").strip()
            elif (count == 5):
                player2_algo = int (line)
            elif (count == 6):
                depth_player2 = int (line)
            elif (count >= 7 and count < 12):
                fill_int_list (line, count-7)
            elif (count >= 12 and count < 17):
                fill_char_list (line, count-12)
            count = count + 1

    except FileNotFoundError:
        print ("Entered file not found\n")


def check_syntax (input):
    if (len (input) != 3):
        print ("Syntax: ./hw1cs561s16.py -i <filename>")
        exit()
    elif (input[1] != "-i"):
        print ("Syntax: ./hw1cs561s16.py -i <filename>")
        exit()

def update_board (temp_cur_board, index, call_type, player1, player2):
    i = int(index) / 10
    j = int(index) % 10

    temp_cur_board[i][j] = player1
    if (get_type (i, j, player1, temp_cur_board) == 1):
        conquer_pawn (temp_cur_board, i, j, player1, player2)

def update_traverse_file():
    global traverse_file
    try:
        traverse_file = open ("traverse_log.txt", "w")
    except FileNotFoundError:
        print ("File does not exist")


def MAX_VALUE (temp_cur_board, cur_depth, parent_index):
    max_value = -sys.maxint - 1
    list = []

    #print ("In MAX_VALUE %d" % (cur_depth))
    get_list (temp_cur_board, list)
    if (0 == len(list) or 0 == cur_depth):
        eval_value = get_eval_value (temp_cur_board)
        traverse_file.write ("%s,%d,%d\n" % (print_next_move_i (parent_index), (cutoff_depth - cur_depth), eval_value))
        return (eval_value)

    traverse_file.write ("%s,%d,-Infinity\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth))))
    for index in list:
        temp_cur_board_max = [row[:] for row in temp_cur_board]
        update_board (temp_cur_board_max, index, "maxvalue", player1, player2)
        #print ("%s" % print_next_move_i (index))
        temp = MIN_VALUE (temp_cur_board_max, cur_depth - 1, index)
        if (temp > max_value):
            max_value = temp
        traverse_file.write ("%s,%d,%d\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth)), max_value))
    return max_value


def MIN_VALUE (temp_cur_board, cur_depth, parent_index):
    min_value = sys.maxint
    list = []

    #print ("In MIN_VALUE %d" % cur_depth)
    get_list (temp_cur_board, list)
    if (0 == len(list) or 0 == cur_depth):
        eval_value = get_eval_value (temp_cur_board)
        traverse_file.write ("%s,%d,%d\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth)), eval_value))
        return (eval_value)

    traverse_file.write ("%s,%d,Infinity\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth))))
    for index in list:
        temp_cur_board_min = [row[:] for row in temp_cur_board]
        update_board (temp_cur_board_min, index, "minvalue", player2, player1)
        #print_board_matrix (temp_cur_board_min)
        temp = MAX_VALUE (temp_cur_board_min, cur_depth - 1, index)
        if (temp < min_value):
            min_value = temp
        traverse_file.write ("%s,%d,%d\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth)), min_value))
    return min_value

def mini_max():
    max_value = -sys.maxint - 1
    temp = 0
    list = []
    cur_depth = cutoff_depth
    #print ("Cur depth = %d" % (cur_depth)) #TODO
    max_i = 0
    max_j = 0

    get_list (cur_board, list)
    if (len(list) == 0):
        return
    update_traverse_file ()
    #print ("In MINI_max")
    #print ("Node,Depth,Value")
    traverse_file.write ("Node,Depth,Value\n")
    #print ("root,0,-Infinity")
    traverse_file.write ("root,0,-Infinity\n")
    for index in list:
        temp_cur_board = [row[:] for row in cur_board]
        update_board (temp_cur_board, index, "mini_max", player1, player2)
        #print_board_matrix (temp_cur_board)
        temp = MIN_VALUE (temp_cur_board, cur_depth - 1, index)
        #print ("%s,1,%d" % (print_next_move_i (index), (temp)))
        if (temp > max_value):
            max_value = temp
            max_i = int(index)/10
            max_j = int(index)%10
        #print ("root,0,%d" % (max_value))
        traverse_file.write ("root,0,%d\n" % (max_value))

    #print ("Final move: "),
    #print ("%s" % print_next_move (max_i, max_j))

    cur_board[max_i][max_j] = player1
    if (get_type (max_i, max_j, player1, cur_board) == 1):
        conquer_pawn (cur_board, max_i, max_j, player1, player2)
    #print_board_matrix(cur_board)
    if (task_number != 4):
        print_to_file (cur_board)
    else:
        print_to_battle_file (cur_board)

def fill_string (alpha, beta):
    if (alpha == -sys.maxint - 1):
        alpha_str = "-Infinity"
    else:
        alpha_str = str(alpha)

    if (beta == sys.maxint):
        beta_str = "Infinity"
    else:
        beta_str = str(beta)

    return (alpha_str, beta_str)

def ALPHA_MAX_VALUE (temp_cur_board, cur_depth, parent_index, alpha, beta):
    max_value = -sys.maxint - 1
    list = []
    alpha_str = ""
    beta_str = ""

    #print ("In MAX_VALUE %d" % (cur_depth))
    get_list (temp_cur_board, list)
    if (0 == len(list) or 0 == cur_depth):
        eval_value = get_eval_value (temp_cur_board)
        (alpha_str, beta_str) = fill_string (alpha, beta)
        traverse_file.write ("%s,%d,%d,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - cur_depth), eval_value, alpha_str, beta_str))
        return (eval_value)

    (alpha_str, beta_str) = fill_string (alpha, beta)
    traverse_file.write ("%s,%d,-Infinity,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - cur_depth), alpha_str, beta_str))
    for index in list:
        temp_cur_board_max = [row[:] for row in temp_cur_board]
        update_board (temp_cur_board_max, index, "maxvalue", player1, player2)
        #print ("%s", print_next_move_i (index))
        temp = ALPHA_MIN_VALUE (temp_cur_board_max, cur_depth - 1, index, alpha, beta)
        if (temp > max_value):
            max_value = temp

        if (max_value >= beta):
            (alpha_str, beta_str) = fill_string (alpha, beta)
            traverse_file.write ("%s,%d,%d,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - cur_depth), max_value, alpha_str, beta_str))
            return max_value

        alpha = max (max_value, alpha)

        (alpha_str, beta_str) = fill_string (alpha, beta)
        traverse_file.write ("%s,%d,%d,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - cur_depth), max_value, alpha_str, beta_str))

    return max_value


def ALPHA_MIN_VALUE (temp_cur_board, cur_depth, parent_index, alpha, beta):
    min_value = sys.maxint
    list = []
    alpha_str = ""
    beta_str = ""

    #print ("In MIN_VALUE %d" % cur_depth)
    get_list (temp_cur_board, list)
    if (0 == len(list) or 0 == cur_depth):
        eval_value = get_eval_value (temp_cur_board)
        (alpha_str, beta_str) = fill_string (alpha, beta)
        traverse_file.write ("%s,%d,%d,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - cur_depth), eval_value, alpha_str, beta_str))
        return (eval_value)

    (alpha_str, beta_str) = fill_string (alpha, beta)
    traverse_file.write ("%s,%d,Infinity,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth)), alpha_str, beta_str))
    for index in list:
        temp_cur_board_min = [row[:] for row in temp_cur_board]
        update_board (temp_cur_board_min, index, "minvalue", player2, player1)
        #print_board_matrix (temp_cur_board_min)
        temp = ALPHA_MAX_VALUE (temp_cur_board_min, cur_depth - 1, index, alpha, beta)
        if (temp < min_value):
            min_value = temp

        if (min_value <= alpha):
            (alpha_str, beta_str) = fill_string (alpha, beta)
            traverse_file.write ("%s,%d,%d,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth)), min_value, alpha_str, beta_str))
            return min_value

        beta = min (min_value, beta)

        (alpha_str, beta_str) = fill_string (alpha, beta)
        traverse_file.write ("%s,%d,%d,%s,%s\n" % (print_next_move_i (parent_index), (cutoff_depth - (cur_depth)), min_value, alpha_str, beta_str))


    return min_value


def ALPHA_BETA():
    max_value = -sys.maxint - 1
    temp = 0
    list = []
    cur_depth = cutoff_depth
    max_i = 0
    max_j = 0
    alpha = -sys.maxint - 1
    beta = sys.maxint
    alpha_str = ""
    beta_str = ""

    get_list (cur_board, list)
    if (len(list) == 0):
        return
    update_traverse_file ()
    traverse_file.write ("Node,Depth,Value,Alpha,Beta\n")
    traverse_file.write ("root,0,-Infinity,-Infinity,Infinity\n")
    for index in list:
        temp_cur_board = [row[:] for row in cur_board]
        update_board (temp_cur_board, index, "mini_max", player1, player2)
        #print_board_matrix (temp_cur_board)
        temp = ALPHA_MIN_VALUE (temp_cur_board, cur_depth - 1, index, alpha, beta)
        if (temp > max_value):
            max_value = temp
            max_i = int(index)/10
            max_j = int(index)%10
        alpha = max_value #TODO

        (alpha_str, beta_str) = fill_string (alpha, beta)
        traverse_file.write ("root,0,%d,%s,%s\n" % (max_value,alpha_str,beta_str))

    #print ("Final move: "),
    #print ("%s" % print_next_move (max_i, max_j))

    cur_board[max_i][max_j] = player1
    if (get_type (max_i, max_j, player1, cur_board) == 1):
        conquer_pawn (cur_board, max_i, max_j, player1, player2)
    #print_board_matrix(cur_board)
    if (task_number != 4):
        print_to_file (cur_board)
    else:
        print_to_battle_file (cur_board)


def fill_player1_info ():
    global player1
    global player2
    global cutoff_depth

    player1 = player1_battle
    player2 = player2_battle
    cutoff_depth = depth_player1

def fill_player2_info ():
    global player1
    global player2
    global cutoff_depth

    player1 = player2_battle
    player2 = player1_battle
    cutoff_depth = depth_player2

def call_algo(algo):
    if (algo == 1):
        #print ("Best first called")
        best_first()
    elif (algo == 2):
        #print ("Mini_max called")
        mini_max()
    elif (algo == 3):
        #print ("Alpha Beta called")
        ALPHA_BETA()

def FIGHT_ON():
    list = []

    get_list (cur_board, list)
    for count in range(len(list)):
        if (count % 2 == 0):
            #print ("Player1")
            fill_player1_info ()
            call_algo (player1_algo)
        if (count % 2 == 1):
            #print ("Player2")
            fill_player2_info ()
            call_algo (player2_algo)


def main():
    check_syntax (sys.argv)
    with open(sys.argv[2], 'r') as f:
        first_line = f.readline()
        task_number_temp = int (first_line)
    #print_value (task_number, cutoff_depth, grid_value, cur_board)
    if (task_number_temp == 1):
        #for i in range (1, star_count+1):
        process_the_file (sys.argv[2])
        best_first()
    elif (task_number_temp == 2):
        process_the_file (sys.argv[2])
        mini_max()
    elif (task_number_temp == 3):
        process_the_file (sys.argv[2])
        ALPHA_BETA()
    elif (task_number_temp == 4):
        open_battle_file()
        process_game_file (sys.argv[2])
        FIGHT_ON ()

if __name__ == "__main__":
    main()
