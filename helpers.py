import random

def initializeBoard():
    board =[]
    for i in range(4):
        row = []
        for j in range(4):
            row.append(0)
        board.append(row)

    # add 2 to a random row & col two times
    numberOfTwos = 0
    while numberOfTwos < 2:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        board[row][col] = 2
        
        numberOfTwos = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] == 2:
                    numberOfTwos += 1
    return board

def printBoard(board):
    for row in board:
        for num in row:
            if num == 0:
                print("    ", end=f"|")
            else:
                print(f"{num:4d}", end=f"|")
        print()
    print()

# reverse the entire board
def reverse(board):
    for i in range(4):
        board[i] = board[i][::-1]

# transpose the entire board
def transpose(board):
    for i in range(4):
        for j in range(i, 4):
            (board[i][j], board[j][i]) = (board[j][i], board[i][j])

# mimics a swipe to left action
'''
input:
    board = [
        [2, 2, 2, 2],
        [2, 0, 2, 2],
        [2, 0, 0, 0],
        [0, 0, 0, 0],
    ]
output:
    board = [
        [4, 4, 0, 0],
        [4, 2, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 0],
    ]
'''
def swipeToLeft(board):
    # move one row to left, without merging the numbers.
    def moveAllNumbersToLeftWithoutMerging(row):
        # move all the numbers to left, without merging
        '''
        we need to do it 3 times, 
        because for row like [0, 2, 2, 2], we need to merge 3 times to be [2, 2, 2, 0]
        '''
        for _ in range(3):
            # iterate from last column to second column
            for currentCol in range(3, 0, -1):
                leftNum = row[currentCol - 1]
                if leftNum == 0:
                    row[currentCol - 1] = row[currentCol]
                    row[currentCol] = 0

    for i in range(4):
        row = board[i]
        moveAllNumbersToLeftWithoutMerging(row)

        # merge values. e.g. for [2, 2, 2, 4], we want it to be [4, 0, 2, 4]
        for currentCol in range(3):
            rightNum = row[currentCol + 1]
            if rightNum == row[currentCol] and rightNum != 0:
                row[currentCol] = row[currentCol] * 2
                row[currentCol + 1] = 0
        
        # move to left again after merging
        moveAllNumbersToLeftWithoutMerging(row)

# mimics a swipe to right action
def swipeToRight(board):
    reverse(board)
    swipeToLeft(board)
    reverse(board)

# mimics a swipe to up action
def swipeToUp(board):
    # transposes the whole board, merges it all left, and then transposes it back
    transpose(board)
    swipeToLeft(board)
    transpose(board)

# mimics a swipe to down action
def swipeToDown(board):
    # transposes the whole board, merges it all right, and then transposes it back
    transpose(board)
    swipeToRight(board)
    transpose(board)
    return board

# add a 2 to a random empty cell in the board, if any
def randomlyAdd2ToBoardIfNotFull(board):
    valid = False
    for i in range(4):
        if 0 in board[i]:
            valid = True
            break
    if not valid:
        # The board is full, early return.
        return
    
    rowNum = random.randint(0, 3)
    colNum = random.randint(0, 3)

    while board[rowNum][colNum] != 0:
        rowNum = random.randint(0, 3)
        colNum = random.randint(0, 3)

    # add 2 to the randomly picked empty cell
    board[rowNum][colNum] = 2

# check whether we should proceed with the game or the user wins/loses the game
# 3 possible values: "UNDETERMINED", "SUCCESS", "FAIL"
def getBoardState(board):
    # SUCCESS if there is a 2048 in the board
    for i in range(4):
        if 2048 in board[i]:
            return "SUCCESS"
 
    # UNDETERMINED if there is an empty cell
    for i in range(4):
        if 0 in board[i]:
            return "UNDETERMINED"
 
    # when we are here, no cell is empty in the board.
    # we should try to see if it is possible to merge any cell 
    # 1) if not possible, then we failed (FAIL)
    # 2) if possible, then we can continue (UNDETERMINED)
        
    # check if we can swipe left or right
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                return "UNDETERMINED"
        
    # check if we can swipe up or down
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j]:
                return "UNDETERMINED"

    # otherwise, we lost the game
    return "FAIL"