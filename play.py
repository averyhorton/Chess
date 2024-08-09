DEBUG = True # defining the DEBUG variable for the play file

if DEBUG:
    print("PLAY    | Play imported!")

def checkWhiteInput(move : str, board : list):
    # error checking
    if not move:
        return None # we are given invalid input
    
    # used for checking and clarifying 
    piece = None
    square = None
    captures = False

    # first, check for castling notation
    if move == 'O-O':
        return ('K', 'g1', False)
    elif move == 'O-O-O':
        return ('K', 'c1', False)
    
    # if not castling notation, assign proper piece value
    if move[0] < 'a':
        if DEBUG:
            print("PLAY    | given a piece!")
        # we are given an uppercase letter, check if it is a valid piece
        if move[0] not in ['R', 'N', 'B', 'Q', 'K', 'P']:
            if DEBUG:
                print("PLAY    | piece was invalid.")
            return None # we are given an invalid piece
        else:
            if DEBUG:
                print("PLAY    | piece was valid!")
            piece = move[0] # piece was in the valid list, save it
            move = move[1:] # shift input for parsing
    elif move[0] < 'i':
        if DEBUG:
            print("PLAY    | given a pawn!")
        # we are given a pawn move, assign pawn to piece
        piece = 'P'
    else:
        if DEBUG:
            print("PLAY    | given invalid piece notation.")
        return None # we are given invalid piece notation
    
    # figure out if captures occured
    if not move:
        if DEBUG:
            print("PLAY    | given invalid input after piece.")
        return None # we are only given a piece
    if (move[0] == 'x' and len(move[1:]) == 2) or (piece == 'P' and len(move) >= 2 and move[1] == 'x' and len(move[2:]) == 2):
        if DEBUG:
            print("PLAY    | given captures!")
        captures = True
        move = move[move.index('x')+1:] # shift input for square parsing
    elif move[0] == 'x':
        if DEBUG:
            print("PLAY    | captures specified, but invalid input after.")
        return None # captures specified, but no valid input after
    
    # check if the final input is a valid square
    if DEBUG:
        print(f"PLAY    | square : {move}") 
    if len(move) != 2:
        # check to see if we're promoting
        if piece != 'P':
            if DEBUG:
                print("PLAY    | invalid input given after piece and captures specification.") 
            return None # promotion returned with non-pawn piece
        else:
            # check if promotion text is specified
            if len(move) == 4 and move[2] == '=' and move[3] in ['R', 'N', 'B', 'Q', 'K', 'P']:
                # we are promoting, move on to square checking
                if DEBUG:
                    print("PLAY    | a pawn is promoting!")
            else:
                # we are not promoting
                if DEBUG:
                    print("PLAY    | invalid promotion field.")
                return None # we are given bad input
    if move[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if DEBUG:
            print("PLAY    | invalid file specified.")
        return None # we are given a bad file
    if move[1] not in ['1','2','3','4','5','6','7','8']:
        if DEBUG:
            print("PLAY    | invalid rank specified.")
        return None # we are given a bad rank


    # we are given valid input, return it
    square = move[0:2]
    return (piece, square, captures)
        