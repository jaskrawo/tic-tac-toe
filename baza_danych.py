
#pycharm ctrl + r do zamiany wielu zwrotów, w VSC ctrl + f (wyszukuje), ctrl + h (zamienia)
import wszystkie_dane
import json


def board_sort(ruch_n):


    tablica_ruch_X=[[], [], [], [], []]
    tablica_ruch_O=[[], [], [], []]

    tablica_ruch = (tablica_ruch_X, tablica_ruch_O)



    for i in ruch_n:
        if i.get('board').count('X')==1 and i.get('board').count('O')==0:
            tablica_ruch_X[0].append(i)


        elif i.get('board').count('X')==1 and i.get('board').count('O')==1:
            tablica_ruch_O[0].append(i)

        elif i.get('board').count('X')==2 and i.get('board').count('O')==1:
            tablica_ruch_X[1].append(i)

        elif i.get('board').count('X')==2 and i.get('board').count('O')==2:
            tablica_ruch_O[1].append(i)

        elif i.get('board').count('X')==3 and i.get('board').count('O')==2:
            tablica_ruch_X[2].append(i)

        elif i.get('board').count('X')==3 and i.get('board').count('O')==3:
            tablica_ruch_O[2].append(i)

        elif i.get('board').count('X')==4 and i.get('board').count('O')==3:
            tablica_ruch_X[3].append(i)

        elif i.get('board').count('X')==4 and i.get('board').count('O')==4:
            tablica_ruch_O[3].append(i)

        elif i.get('board').count('X')==5 and i.get('board').count('O')==4:
            tablica_ruch_X[4].append(i)

        else:
            continue

    return tablica_ruch

def zapis(tablica_ruch):
    with open('zapis_plansz.txt', 'w') as f:
        json.dump(tablica_ruch, f)




