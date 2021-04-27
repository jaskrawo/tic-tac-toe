

import itertools

def board_init():

    ruch_n = []

    for b,i in enumerate(itertools.product(' XO', repeat=9)):

        if b==100000:
            break
        else:
            ruch_n_nr = {'numer': b, 'board': i, 'value': 100}
            ruch_n.append(ruch_n_nr)

    return ruch_n





