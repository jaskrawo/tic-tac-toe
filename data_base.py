import all_data
import json

#board_sort module sorts and filters list created with board_init() in the all_data module
def board_sort(move_n):

    #move_list_X and move_list_O are used to sort moves by sign and number, from first to fifth in Xs and fourth in Os.
    move_list_X=[[], [], [], [], []]
    move_list_O=[[], [], [], []]

    move_list = (move_list_X, move_list_O)



    for i in move_n:
        if i.get('board').count('X')==1 and i.get('board').count('O')==0:
            move_list_X[0].append(i)


        elif i.get('board').count('X')==1 and i.get('board').count('O')==1:
            move_list_O[0].append(i)

        elif i.get('board').count('X')==2 and i.get('board').count('O')==1:
            move_list_X[1].append(i)

        elif i.get('board').count('X')==2 and i.get('board').count('O')==2:
            move_list_O[1].append(i)

        elif i.get('board').count('X')==3 and i.get('board').count('O')==2:
            move_list_X[2].append(i)

        elif i.get('board').count('X')==3 and i.get('board').count('O')==3:
            move_list_O[2].append(i)

        elif i.get('board').count('X')==4 and i.get('board').count('O')==3:
            move_list_X[3].append(i)

        elif i.get('board').count('X')==4 and i.get('board').count('O')==4:
            move_list_O[3].append(i)

        elif i.get('board').count('X')==5 and i.get('board').count('O')==4:
            move_list_X[4].append(i)

        else:
            continue

    return move_list

def save(move_list):
    with open('all_moves.txt', 'w') as f:
        json.dump(move_list, f)
