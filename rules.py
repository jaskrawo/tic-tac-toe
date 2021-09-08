import random
import json
import all_data
import data_base




try:

    with open('all_moves.txt') as json_file:
        move_list = json.load(json_file)

except IOError:
    move_n = all_data.board_init()
    move_list = data_base.board_sort(move_n)




def iswin(board, letter='X'):

    if board[0]==letter and board[1]==letter and board[2]==letter:
        return True
    elif board[3]==letter and  board[4]==letter and board[5]==letter:
        return True
    elif board[6] == letter and board[7] == letter and board[8] == letter:
        return True
    elif board[0] == letter and board[3] == letter and board[6] == letter:
        return True
    elif board[1] == letter and board[4] == letter and board[7] == letter:
        return True
    elif board[2] == letter and board[5] == letter and board[8] == letter:
        return True
    elif board[0] == letter and board[4] == letter and board[8] == letter:
        return True
    elif board[6] == letter and board[4] == letter and board[2] == letter:
        return True
    else:
        return False






def draw(letter, number, board):
    possible_moves=[]
    move = move_list[letter][number]

    for i in move:

        sum=0

        for z, g in zip(i['board'], board[0]['board']):

            if z==g:
                continue
            else:
                sum += 1
        if sum==1:
            possible_moves.append(i)
        else:
            continue

    return(random.choices(possible_moves, weights=[i['value'] for i in possible_moves], k = 1))




def save():
    with open('all_moves.txt', 'w') as f:
        json.dump(move_list, f)
