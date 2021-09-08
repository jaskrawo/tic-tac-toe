import rules


for i in range (1):

    moves_x = []
    moves_O = []

    board = [{'number': 100000, 'board': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 'value': 100}]
    move_X = True
    move_O = False
    change = 0
    while True:
        if move_X and change <= 4:

            board = rules.draw(0, change, board)
            moves_X.append(board)

            print(board[0]['board'][:3])
            print(board[0]['board'][3:6])
            print(board[0]['board'][6:])



            move_X = False
            move_O = True

            if (rules.iswin(board[0]['board'], 'X')):

                print(board[0]['board'][:3])
                print(board[0]['board'][3:6])
                print(board[0]['board'][6:])
                print('X won!')




                for move in moves_X:
                    move[0]['value'] += 1

                for move in moves_O:
                    if move[0]['value'] > 1:
                        move[0]['value'] -= 1

                break

        elif move_O and change<4:
            board = rules.draw(1, change, board)

            print(board[0]['board'][:3])
            print(board[0]['board'][3:6])
            print(board[0]['board'][6:])



            zestaw_O.append(board)
            move_X = True
            move_O = False

            change += 1
            if (zasady.iswin(board[0]['board'], 'O')):

                print(board[0]['board'][:3])
                print(board[0]['board'][3:6])
                print(board[0]['board'][6:])
                print('O won!')



                for move in moves_O:
                        move[0]['value'] += 1

                for move in moves_X:
                    if move[0]['value'] > 1:
                        move[0]['value'] -= 1

                break


        else:
            print('Draw!')


            break


rules.zapis()

