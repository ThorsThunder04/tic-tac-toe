"""
Game written by Thor.N from scratch.
Project started on 16/07/2021 at 00:07.
"""
import os



clear = lambda: os.system('cls')

pause = lambda: input('\nPress Enter to continue...')


def check_winner(board):

        #checks all the rows for a winner
        def check_rows(input):
            for row in input:
                if row.count('X') == len(row):
                    return 'X'
                elif row.count('O') == len(row):
                    return 'O'
        
        #check's all the columns for a winner
        def check_columns():
            transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
            check_rows(transposed_board)
        
        def check_diagonals():
            if len(set([board[0][0], board[1][1], board[2][2]])) == 1:
                return board[1][1]
            elif len(set([board[0][2], board[1][1], board[2][0]])) == 1:
                return board[1][1]
                

        if (check_rows(board) == "X") or (check_columns() == "X") or (check_diagonals() == 'X'):
            return 'X'
        elif (check_rows(board) == 'O') or (check_columns() == 'O') or (check_diagonals() == 'O'):
            return 'O'



def main():

    



    currentBoard = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    #conversion for the coordinates
    coordDict = {
        'a': 0, 'b': 1, 'c': 2,
        '1':0, '2':1, '3':2
    }




    print('\nThe starting player is X.')
    print('You must enter the correct cordinates to place your symbol.')
    print('Have fun!')


    input('\nPress Enter to begin the game...')
    clear()

    winner = ''

    playerTurn = 'X'
    # starts the game proccess
    while (winner != 'X') or (winner != 'O'):
        
        #checks for a winner
        if (check_winner(currentBoard) == 'X') or (check_winner(currentBoard) == 'O'):
            winner = check_winner(currentBoard)
            break

        else:

            #prints big X or O
            if playerTurn == 'X':
                print('\  / \n \/ \n /\ \n/  \ \n')
            elif playerTurn == 'O':
                print(' ---- \n|    | \n|    | \n ---- \n')



            #prints the grid with the symbols in place
            print('a:  '+currentBoard[0][0]+' | '+currentBoard[0][1]+' | '+currentBoard[0][2])
            print('   -----------')
            print('b:  '+currentBoard[1][0]+' | '+currentBoard[1][1]+' | '+currentBoard[1][2])
            print('   -----------')
            print('c:  '+currentBoard[2][0]+' | '+currentBoard[2][1]+' | '+currentBoard[2][2])
            print('    1   2  3')
            
            #asks for a coordinate to place the symbol
            symbolCoord = input('Enter your symbole coordinate (ex: a2) : ').lower()
            
            #updates the grid
            if (symbolCoord[0] in coordDict) and (symbolCoord[1] in coordDict) and (currentBoard[coordDict[symbolCoord[0]]][coordDict[symbolCoord[1]]] == ' '):
                if (playerTurn == 'X'):
                    currentBoard[coordDict[symbolCoord[0]]][coordDict[symbolCoord[1]]] = 'X'
                    playerTurn = 'O' #switches the player's turn
                
                elif (playerTurn == 'O'):
                    currentBoard[coordDict[symbolCoord[0]]][coordDict[symbolCoord[1]]] = 'O'
                    playerTurn = 'X' #switches the player's turn
            else:
                #if a player enters an invalid coordinate
                print('Sorry that is not a valid coordinate')
                input('Press Enter to try again...')
                clear()
                continue

            clear()

    print(' ')
    print('Congrats, the winner of the game is player', winner, '!!!')

clear()

main()

#asks if player wants to play again
keepPlaying = True
while keepPlaying:
    print('Would you like to play again?')
    choice = input('\ny for yes, n for no :')
    if choice == 'y':
        main()
    elif choice == 'n':
        keepPlaying = False
    else:
        clear()
        print('\nPlease enter a valid answer.')
        input('\nPress Enter to answer again...')
