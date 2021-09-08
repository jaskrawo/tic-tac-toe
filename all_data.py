import itertools

def board_init():

    move_number = []

    for b,i in enumerate(itertools.product(' XO', repeat=9)):

        if b==100000:
            break
        else:
            move_n_number = {'number': b, 'board': i, 'value': 100}
            move_number.append(move_n_number)

    return move_number
