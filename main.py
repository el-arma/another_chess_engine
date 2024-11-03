# CHESS ENGINE
# v.1.0.0

from enum import Enum
import numpy as np

# Set the print options in numpy so that the chess boards print nicely: 
np.set_printoptions(edgeitems = 30, linewidth = 250, formatter = dict(float = lambda x: "%.3g" % x))

class Pieces_Types(Enum):
    
    # black pieces symbols:
    WHITE_KING = '♔'
    WHITE_QUEEN = '♕'
    WHITE_TOWER = '♖'
    WHITE_BISHOP = '♗'
    WHITE_KNIGHT = '♘'
    WHITE_PAWN = '♙'

    # black pieces symbols:
    BLACK_KING = '♚'
    BLACK_QUEEN = '♛'
    BLACK_TOWER = '♜'
    BLACK_BISHOP = '♝'
    BLACK_KNIGHT = '♞'
    BLACK_PAWN = '♟'
    
class Pieces_Col(Enum):
    BLACK = 'B'
    WHITE = 'W'

class Tiles(Enum):
    WHITE = ' □ '
    BLACK = ' ■ '

class Alt_Colors(Enum):
    GREEN = '\033[92m'
    ENDC = '\033[0m'




################################################################################################
# TILES:

class Board_tile:

    def __init__(self, tile_white: bool):
        
        self.tile_white = tile_white
        
        if self.tile_white:
            self.symbol = Tiles.WHITE.value
        else:
            self.symbol = Tiles.BLACK.value

    def __repr__(self) -> str:
        return self.symbol

################################################################################################
# GAME PIECES:

class Piece:
    def __init__(self, color: Pieces_Col, name,
                  piece_type: Pieces_Types) -> None:
        
        self.color = color
        self.name = name
        self.piece_type = piece_type
    
    def move(self, field):
        pass

    def possible_moves(self):
        pass

    def __repr__(self) -> str:
        
        if self.color == Pieces_Col.BLACK.value:
            
            prnt_me = f'{Alt_Colors.GREEN.value} {self.piece_type} {Alt_Colors.ENDC.value}'
        
        else:
            
            prnt_me = f' {self.piece_type} '
        
        return prnt_me

class Pawn(Piece):
    pass

class Knight(Piece):
    pass

class Tower(Piece):
    pass

class Queen(Piece):
    pass

class King(Queen):
    pass


################################################################################################
# GAME:

class Game:

    def __init__(self) -> None:
        
        # CREATE EMPTY CHESS BOARD:
        white_tile = Board_tile(True)
        black_tile = Board_tile(False)

        self.board = np.full((8, 8), white_tile, dtype = 'O')

        self.board[::2, 1::2] = black_tile  
        # Setting alternate rows starting from the first row with alternate columns to 

        self.board[1::2, ::2] = black_tile
        # Setting alternate rows starting from the second row with alternate columns to 1

        # PLACE PIECES:
        # (REFACTORISATION REQUIRED!)
        self.board[1,:] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_PAWN.value)
        self.board[6,:] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_PAWN.value)

        self.board[0,7] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_TOWER.value)
        self.board[0,0] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_TOWER.value)

        self.board[7,7] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_TOWER.value)
        self.board[7,0] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_TOWER.value)


        self.board[0,6] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_KNIGHT.value)
        self.board[0,1] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_KNIGHT.value)

        self.board[7,6] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_KING.value)
        self.board[7,1] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_KING.value)

        self.board[0,1] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_KNIGHT.value)
        self.board[0,6] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_KNIGHT.value)

        self.board[7,1] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_KING.value)
        self.board[7,6] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_KING.value)


        self.board[0,2] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_BISHOP.value)
        self.board[0,5] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_BISHOP.value)

        self.board[7,2] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_BISHOP.value)
        self.board[7,5] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_BISHOP.value)


        self.board[0,3] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_QUEEN.value)
        self.board[0,4] = Piece(color = Pieces_Col.BLACK.value, name = 'piece', piece_type = Pieces_Types.BLACK_KING.value)

        self.board[7,3] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_QUEEN.value)
        self.board[7,4] = Piece(color = Pieces_Col.WHITE.value, name = 'piece', piece_type = Pieces_Types.WHITE_KING.value)

    def display_board(self) -> None:

        print()

        for idx, row in enumerate(self.board):
            print(8 - idx, ' ' , row)

        print(' ' * 6 + '-' * 30)
        print(' ' * 6 + 'a   b   c   d   e   f   g   h \n')

        return None




#######################################################################################################################
if __name__ == "__main__":

    g1 = Game()

    g1.display_board()


