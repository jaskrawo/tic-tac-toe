import zasady


for i in range (1):

    zestaw_X = []
    zestaw_O = []

    board = [{'numer': 100000, 'board': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 'value': 100}]
    tura_X = True
    tura_O = False
    zmiana = 0
    while True:
        if tura_X and zmiana <= 4:

            board = zasady.losowanie(0, zmiana, board)
            zestaw_X.append(board)

            print(board[0]['board'][:3])
            print(board[0]['board'][3:6])
            print(board[0]['board'][6:])
            print('wygrało kółko')



            tura_X = False
            tura_O = True

            #wygrał X
            if (zasady.iswin(board[0]['board'], 'X')):

                print(board[0]['board'][:3])
                print(board[0]['board'][3:6])
                print(board[0]['board'][6:])
                print('wygrał krzyżyk')




                for move in zestaw_X:
                    move[0]['value'] += 1

                for move in zestaw_O:
                    if move[0]['value'] > 1:
                        move[0]['value'] -= 1

                break

        elif tura_O and zmiana<4:
            board = zasady.losowanie(1, zmiana, board)

            print(board[0]['board'][:3])
            print(board[0]['board'][3:6])
            print(board[0]['board'][6:])
            print('wygrało kółko')



            zestaw_O.append(board)
            tura_X = True
            tura_O = False

            zmiana += 1
            if (zasady.iswin(board[0]['board'], 'O')):

                print(board[0]['board'][:3])
                print(board[0]['board'][3:6])
                print(board[0]['board'][6:])
                print('wygrało kółko')



                for move in zestaw_O:
                        move[0]['value'] += 1

                for move in zestaw_X:
                    if move[0]['value'] > 1:
                        move[0]['value'] -= 1

                break


        else:
            print('Remis')


            break


zasady.zapis()

