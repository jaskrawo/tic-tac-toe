import random
import json
import all_data
import data_base



#if there is no file 'all_moves.txt' it is is created 
try:

    with open('all_moves.txt') as json_file:
        move_list = json.load(json_file)

except IOError:
    move_n = all_data.board_init()
    move_list = data_base.board_sort(move_n)



#iswin function is used to check if Xs or Os have alredy won
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





#draw function is used to draw a move from a list of possible moves
#the probability of each choice is dependent on previous results
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



#saves changes made in the 'all_moves.txt' file
def save():
    with open('all_moves.txt', 'w') as f:
        json.dump(move_list, f)

#function used to visualize present state of the board
def draw_board(board):
    return(
    '''
{}
{}
{}

    '''.format(board[0]['board'][:3], board[0]['board'][3:6], board[0]['board'][6:])
    )
