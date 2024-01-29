import helpers
from copy import deepcopy

board = helpers.initializeBoard()

print("\nWelcome to Sylvia's 2048 game...\n")
print("Here is your board:")
helpers.printBoard(board)
print("Please enter w,s,a,d to move your board. Enjoy your game!\n")

isGameEnded = False
while not isGameEnded:
    direction = input("Move started: Do you want to move up/down/left/right? (Please enter one of w,s,a,d)\n").strip()
    try:
        originalBoard = deepcopy(board)
        if direction == 'd':
            helpers.swipeToRight(board)
        elif direction == 'w':
            helpers.swipeToUp(board)
        elif direction == 'a':
            helpers.swipeToLeft(board)
        elif direction == 's':
            helpers.swipeToDown(board)
        else:
            raise ValueError("\nInvalid input. Please enter one of w,s,a,d.")
        if originalBoard == board:
            raise ValueError("\nInvalid input. You can not move with this direction.")
        helpers.randomlyAdd2ToBoardIfNotFull(board)
    except ValueError as error:
        print(error)
        print()
        continue
    
    print()
    state = helpers.getBoardState(board)
    if state == "SUCCESS":
        print("Congrats!!! YOU WON THE GAME!!!")
        helpers.printBoard(board)
        isGameEnded = True
    elif state == "UNDETERMINED":
        print("Here is your current board:")
        helpers.printBoard(board)
    elif state == "FAIL":
        print("OH NO! You have failed the game, but good job!!!")
        helpers.printBoard(board)
        isGameEnded = True

print("\nGAME ENDED.....")
    