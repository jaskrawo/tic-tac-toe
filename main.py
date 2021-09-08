import rules

#main game loop. Number of repetition defines how many games are played
for i in range (1):

    #these two lists are used to store moves used in each game
    moves_X = []
    moves_O = []

    #creation of an empty board, flags move_X and move_O are used to define whether it is Xs or Os move at the moment
    board = [{'number': 100000, 'board': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 'value': 100}]
    move_X = True
    move_O = False
    #change flag is the cap that prevents the game to be played for longher than 9 moves
    change = 0

    #this loop goes on until Os or Xs wins or it is a draw
    while True:


        if move_X and change <= 4:

            #to define new board after Xs move we use function called draw() defined in the rules module
            board = rules.draw(0, change, board)
            moves_X.append(board)

            #to visualize the game we use draw_board() function defined in rules module
            print(rules.draw_board(board))



            move_X = False
            move_O = True

            #using iswin function from rules() we check if Xs have alredy won
            if (rules.iswin(board[0]['board'], 'X')):

                print(rules.draw_board(board))
                print('X won!')



                #if Xs won we add points to all of Xs moves from that game
                #and take points from Os moves
                for move in moves_X:
                    move[0]['value'] += 1

                for move in moves_O:
                    if move[0]['value'] > 1:
                        move[0]['value'] -= 1

                break

        #next O play its move
        elif move_O and change<4:
            board = rules.draw(1, change, board)

            print(rules.draw_board(board))

            moves_O.append(board)
            move_X = True
            move_O = False

            change += 1
            if (rules.iswin(board[0]['board'], 'O')):

                print(rules.draw_board(board))
                print('O won!')



                for move in moves_O:
                        move[0]['value'] += 1

                for move in moves_X:
                    if move[0]['value'] > 1:
                        move[0]['value'] -= 1

                break

        #if the board is full and neither of the players won
        else:
            print('Draw!')
            break


#after compliton of the main game loop we save the results
rules.save()

