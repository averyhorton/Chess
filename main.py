# import the setup, engine, and play packages, as well as some python libraries
import play, engine, helpers

# setup the DEBUG variable for main (True = ON, False = OFF)
DEBUG = True

# setup the engine (True = use Stockfish 16, False = use default)
ENGINE = True

# specify whether you want FEN notation printed with the board
FEN = True

if __name__ == "__main__":
    # initialize helper variables for use in FEN translation
    fen_notation = None # to hold the FEN notation
    to_move = 'w' # 'w' denotates white to move, 'b' black to move
    white_castling = 'KQ' # - : no castling, K : kingside castling, Q : queenside castling
    black_castling = 'kq' # - : no castling, k : kingside castling, q : queenside castling
    en_passant = '-' # '-' denotates no en passant possible, otherwise one square is specified
    half_moves = 1 # number of turns 
    full_moves = 0 # number of total moves

    # initialize helper variables for assistance in piece moving
    # castling booleans
    white_Kcastling_blocked = True # denotates whether white has pieces blocking it from castling kingside
    white_Qcastling_blocked = True # denotates whether white has pieces blocking it from castling kingside
    white_castling_allowed = True # denotates whether white is still allowed to castle kingside
    black_Kcastling_blocked = True # denotates whether black has pieces blocking it from castling kingside
    black_Qcastling_blocked = True # denotates whether black has pieces blocking it from castling queenside
    black_castling_allowed = True # denotates whether black is still allowed to castle

    # check booleans: used to force a king move
    white_inCheck = False
    black_inCheck = False
    white_checkmated = False
    black_checkmated = False

    # denotates whether each pawn has made its starting move
    # white_start[0] denotates White pawn A, white_start[1] denotates White pawn B, etc.
    white_start = [False, False, False, False, False, False, False, False] 
    # black_start[0] denotates Black pawn A, black_start[1] denotates Black pawn B, etc.
    black_start = [False, False, False, False, False, False, False, False]

    if DEBUG: print("MAIN    | Variables initialized!")

    # initialize the board
    board = helpers.initBoard() # board will be used for displaying the game state and translating to FEN
    fen_notation = helpers.boardToFEN(board) # translate starting position to FEN
    if DEBUG: print("MAIN    | Board successfully set up!")

    # begin game
    while (not white_inCheck) and (not black_inCheck):
        # print board
        print("   WHITE TO MOVE   ")
        helpers.printBoard(board, FEN, fen_notation)

        # get white's desired move
        move = play.checkWhiteInput(input("Enter move here in standard notation: "), board)
        # check the validity of white's move; if invalid, reprompt
        while move == None:
            move = play.checkWhiteInput(input("Invalid notation. Enter move here in standard notation: "), board)

        if DEBUG:
            print(f'MAIN    | {move}')

        # check if the move white was requested is a legal move
            
        # play the move and get black's move
            