DEBUG = False # defining the DEBUG variable for the setup file

if DEBUG:
    print("HELPERS | Setup imported!")

# sets up the game board and returns it
def initBoard():
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

# prints the current state of the board
def printBoard(board : list, FEN : bool, fen : str):
    # print the board
    for r in range(8):
        print("| ", end="")
        for c in range(8):
            print(f'{board[r][c]} ', end='')
        print("|")
    
    # print the FEN notation if fen is defined
    if FEN:
        print(f'\n{fen}')    

# converts the current position stored in board to FEN notation
def boardToFEN(board : list):
    ret = '' # return string holding the FEN notation
    for r in range(8):
        empty_count = 0 # used to print number of empty squares in a row before a piece/the end of the board
        for c in range(8):
            if board[r][c] != " " and empty_count == 0:
                ret += f'{board[r][c]}'
                empty_count = 0
            elif board[r][c] != " ":
                ret += f'{empty_count}{board[r][c]}'
                empty_count = 0
            else:
                empty_count += 1
        if r != 7:
            # determines the appropriate FEN notation based on row number
            if empty_count == 0:       
                ret += "/"
            else:
                ret += f'{empty_count}/'
    
    return ret