import random
import json
import wszystkie_dane
import baza_danych




try:

    with open('zapis_plansz.txt') as json_file:
        tablica_ruch = json.load(json_file)

except IOError:
    ruch_n = wszystkie_dane.board_init()
    tablica_ruch = baza_danych.board_sort(ruch_n)




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






def losowanie(litera, nr, board):
    mozliwe_ruchy=[]
    ruch = tablica_ruch[litera][nr]
    for i in ruch:

        suma=0
        for z, g in zip(i['board'], board[0]['board']):

            if z==g:
                continue
            else:
                suma+=1
        if suma==1:
            mozliwe_ruchy.append(i)
        else:
            continue

    return(random.choices(mozliwe_ruchy, weights=[i['value'] for i in mozliwe_ruchy], k = 1))




def zapis():
    with open('zapis_plansz.txt', 'w') as f:
        json.dump(tablica_ruch, f)







