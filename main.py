def printBoard(board):  # Printing the Game Board
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('- - - ')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('- - - ')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):  # Check if the current position is free or not
    if board[position] == ' ':
        return True  # If It's Free return True
    else:
        return False  # If It's not Free return False


def insertLetter(letter, position):  # This Method to insert X or O letter
    if spaceIsFree(position):  # First we have to check if the position we are going to insert is free
        board[position] = letter  # If it is free then we put the letter on the current position we want to add
        printBoard(board)  # Print the board
        if checkDraw():  # If it is a Draw then Prints Draw and exit
            print("Draw!")
            exit()
        if checkForWin():  # If it is a win then Prints Bot or Player wins depending on the game
            if letter == 'X':  # If the letter was X then the Computer Wins
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")  # Else the Bot Wins
                exit()

        return


    else:  # Else that means that you inserted on a position that is not Empty
        print("Can't insert there!")  # So it prints that you cannot inert here
        position = int(input("Please enter new position:  "))  # and then you enter a new Position
        insertLetter(letter, position)  # and Recursively you check again
        return


def checkForWin():  # This method is to see who won the game, so you can win as same diagonal or same row (X or O)
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(
        mark):  # This method determine which player has Won the game, as example if we pass the X and return True that means that the X wins
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():  # This method is to see if the game is Draw
    for key in board.keys():  # We make a loop to see if there is a place empty on the board or not
        if (board[key] == ' '):  # If there is a place that is empty, it means that the game isn't ended yet and players still can play in this places
            return False  # So it returns False , when there still a place we can put in
    return True  # Else return True when the whole places aren't free, and no one wins


def playerMove():  # Player enters the Position of O
    position = int(input("Enter the position for 'O':  "))  # SO, he enters the position
    insertLetter(player, position)  # Take the player Position by calling Insert Method
    return  # and then return


def compMove():
    bestScore = -800  # We want to Maximise the Score
    bestMove = 0  # It will be random , and be changed later
    for key in board.keys():  # We need to go in every possible Move, so we do a loop for that
        if (board[key] == ' '):  # if the place is empty
            board[key] = bot  # We let the Bot plays first ( X plays first )
            score = minimax(board, 0, False)  # and from the minimax method we determine the Score
            board[key] = ' '  # we want to revert what we did , so we make it empty once again
            if (score > bestScore):
                bestScore = score
                bestMove = key  # because it's the Best Move we played

    insertLetter(bot, bestMove)  # Then we let the players starts, and we give him the bestMove we found
    return


def minimax(board, depth,
            isMaximizing):  # minimax method takes the board state, depth, and we need to know if we are maximizing or minimizing, isMaximising is a boolean Value, we do not need the Depth because it's a small game, only we have 9 moves
    if (checkWhichMarkWon(bot)):  # If bot wins , that's mean he maximized the score so return 1
        return 1
    elif (checkWhichMarkWon(player)):  # If Player wins , that's mean  he minimized the score so return -1
        return -1
    elif (checkDraw()):
        return 0  # return 0 if it's a draw

    if (isMaximizing):  # The X starts first, so he needs to maximize the Score , so as default we give him a low score to find the best move and best score
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)  # Depth doesn't matter we can put it 0
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800  # The O starts first so , he needs no minimise the Score , so as default we give him a high score to minimise it
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',  # Creating the Game Board
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'  # Player plays for O
bot = 'X'  # The Computer plays for X

global firstComputerMove
firstComputerMove = True

while not checkForWin():  # Means that if no one won yet, player plays and computer too.
    compMove()
    playerMove()
