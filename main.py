# CHESS ENGINE
# v.1.0.1


from enum import Enum
import numpy as np

# Set the print options in numpy so that the chess boards print nicely: 
np.set_printoptions(edgeitems = 30, linewidth = 250, formatter = dict(float = lambda x: "%.3g" % x))

class Piece_Icon(Enum):
    
    # white pieces symbols:
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

class Piece_Type(Enum):
    KING = 'king'
    QUEEN = 'queen'
    TOWER = 'tower'
    BISHOP = 'bishop'
    KNIGHT = 'knight'
    PAWN = 'pawn'

class Piece_Col(Enum):
    BLACK = 'B'
    WHITE = 'W'

class Tile(Enum):
    WHITE = ' □ '
    BLACK = ' ■ '

class Alt_Color(Enum):

    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    COLOR_OFF = '\033[0m'

################################################################################################
# TILES:

class Board_tile:

    def __init__(self, tile_white: bool):
        
        self.tile_white = tile_white
        
        if self.tile_white:
            self.symbol = Tile.WHITE.value
        else:
            self.symbol = Tile.BLACK.value

    def __repr__(self) -> str:
        return self.symbol

################################################################################################
# CHESS PIECES:
# probably to be moved to a separate file

class Piece:
    def __init__(self, color: Piece_Col, piece_type: Piece_Type, icon: Piece_Icon) -> None:
        
        self.color = color
        self.piece_type = piece_type
        self.icon = icon
    
    def move(self, field: str) -> None:
        # something like this:
        # 7a>6a (move fig. from field 7a to 6a) we could use ">" operator overload 
        # alternatively or perhapes also use simplyfiy chess nontation:
        # see: https://www.chess.com/terms/chess-notation

        pass

    def possible_moves(self):
        pass

    def __repr__(self) -> str:
        # return garphical representation of a piece
        
        if self.color == Piece_Col.BLACK.value:
            
            prnt_me = f'{Alt_Color.GREEN.value} {self.icon} {Alt_Color.COLOR_OFF.value}'
            # for better viability 'black' are green
        
        else:
            
            prnt_me = f' {self.icon} '
         
        return prnt_me

# remember about super() method:
class Pawn(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Tower(Piece):
    pass

class Queen(Piece):
    pass

class King(Queen):
    pass


################################################################################################
# GAME:

class Player:

    # instance counter:
    inst_cnt = 0

    def __init__(self, player_name: str = None) -> None:
        # much, much later at the end ask player about the name (input())

        self.player_name = player_name

        Player.inst_cnt += 1
        
        if Player.inst_cnt > 2:
            raise Exception("You can't have more then two Players!")

        if self.player_name is None:
            # if a player dont want a name or during unit tests

            self.player_name = f'Player_{Player.inst_cnt}'

        else:
            self.player_name = player_name

        return None

class Spectator:
    # perhapse?
    # definetly not a priority
    pass

class Game:

    def __init__(self) -> None:
        
        self.p1: Player = Player()
        self.p2: Player = Player()

        # CREATE EMPTY CHESS BOARD:
        self.white_tile = Board_tile(True)
        self.black_tile = Board_tile(False)

        # start with all tiles white
        self.board = np.full((8, 8), self.white_tile, dtype = 'O')

        # add black tiles p.1
        self.board[::2, 1::2] = self.black_tile  
        # Setting alternate rows starting from the first row with alternate columns to 

        # add black tiles p.2
        self.board[1::2, ::2] = self.black_tile
        # Setting alternate rows starting from the second row with alternate columns to 1

        # PLACE PIECES ON THE BOARD:
        # (require furhter refactorization)

        self.white_pawn = Pawn(color = Piece_Col.WHITE.value, piece_type = Piece_Type.PAWN.value, 
                               icon = Piece_Icon.WHITE_PAWN.value)
        self.black_pawn = Pawn(color = Piece_Col.BLACK.value, piece_type = Piece_Type.PAWN.value, 
                               icon = Piece_Icon.BLACK_PAWN.value)
        
        self.white_tower =  Tower(color = Piece_Col.WHITE.value, piece_type = Piece_Type.TOWER.value, 
                                  icon = Piece_Icon.WHITE_TOWER.value)
        self.black_tower =  Tower(color = Piece_Col.BLACK.value, piece_type = Piece_Type.TOWER.value, 
                                  icon = Piece_Icon.BLACK_TOWER.value)
        
        self.white_knight = Knight(color = Piece_Col.WHITE.value, piece_type = Piece_Type.KNIGHT.value, 
                                   icon = Piece_Icon.WHITE_KNIGHT.value)
        self.black_knight = Knight(color = Piece_Col.BLACK.value, piece_type = Piece_Type.KNIGHT.value, 
                                   icon = Piece_Icon.BLACK_KNIGHT.value)

        self.white_bishop = Bishop(color = Piece_Col.WHITE.value, piece_type = Piece_Type.BISHOP.value, 
                                   icon = Piece_Icon.WHITE_BISHOP.value)
        self.black_bishop = Bishop(color = Piece_Col.BLACK.value, piece_type = Piece_Type.BISHOP.value, 
                                   icon = Piece_Icon.BLACK_BISHOP.value)

        self.white_queen = Queen(color = Piece_Col.WHITE.value, piece_type = Piece_Type.QUEEN.value, 
                                 icon = Piece_Icon.WHITE_QUEEN.value)
        self.black_queen = Queen(color = Piece_Col.BLACK.value, piece_type = Piece_Type.QUEEN.value, 
                                 icon = Piece_Icon.BLACK_QUEEN.value)

        self.white_king = King(color = Piece_Col.WHITE.value, piece_type = Piece_Type.KING.value, 
                               icon = Piece_Icon.WHITE_KING.value)
        self.black_king = King(color = Piece_Col.BLACK.value, piece_type = Piece_Type.KING.value, 
                               icon = Piece_Icon.BLACK_KING.value)

        # place pawns:
        self.board[1,:] = self.black_pawn
        self.board[6,:] = self.white_pawn
        
        # place towers:
        self.board[0,7] = self.black_tower
        self.board[0,0] = self.black_tower
        self.board[7,0] = self.white_tower
        self.board[7,7] = self.white_tower

        # place knights:
        self.board[0,1] = self.black_knight
        self.board[0,6] = self.black_knight
        self.board[7,1] = self.white_knight
        self.board[7,6] = self.white_knight
        
        # place bishops:
        self.board[0,2] = self.black_bishop
        self.board[0,5] = self.black_bishop
        self.board[7,2] = self.white_bishop
        self.board[7,5] = self.white_bishop

        # place queens:
        self.board[7,3] = self.white_queen
        self.board[0,3] = self.black_queen
        
        # place kings:
        self.board[7,4] = self.white_king
        self.board[0,4] = self.black_king
        

    def display_board(self) -> None:

        print('\n' + ' ' * 6 + '-' * 30)

        for idx, row in enumerate(self.board):
            print(8 - idx, ' ' , row)

        print(' ' * 6 + '-' * 30)
        print(' ' * 6 + 'a   b   c   d   e   f   g   h \n')

        return None




#######################################################################################################################
if __name__ == "__main__":

    g1 = Game()

    g1.display_board()

