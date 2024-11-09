# CHESS ENGINE
# v.1.0.2


from enum import Enum
# for declaring CONST.
import numpy as np
# for chess board
from typing import Tuple
# for better type annotation

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

# TODO:
# later when we have all proper methods
# remember about super() method
# establish universal unit movement on the board no matter of payer perspective
# (e.g. if black pawn can only go down (+1 row on the numpy array), white on the other hand can go only upwad -1 )

class Pawn(Piece):
    # PAWN MOVE SCHEME:
    # if board row == 1 or row == 6 you can move 1 or 2 field forward
    # otherwise only one step ahead
    # (En passant to be implement later)

    def check_move(self, orgn_field_tup: Tuple[int, int], 
                       trgt_field_tup: Tuple[int, int]) -> bool:
        
        """check if a given pawn standing on the orgn_field_tup can move to the trgt_field_tup
            (both: orgn_field_tup trgt_field_tup are numpy array co-ordinates e.g. (0, 0 ))
            board_snapshot provide simplify information what is the situation on the board 
            (later optionaly check all possible moves for that piece)"""
        
        is_possible = None

        return is_possible

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Tower(Piece):
    pass

class Queen(Piece):
    # inherents moves from Bishop and Tower(multiple inherentance)
    pass

class King(Queen):
    # copy moves from Queen but limit it by one
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
    # definetly not a priority
    # Add spectator who could watch the game(perhapse)
    pass

class Game:
# Should we extract new class Board from from Game class?


    def __init__(self) -> None:
        
        self.p1: Player = Player()
        self.p2: Player = Player()

        # CREATE EMPTY CHESS BOARD:
        self.white_tile = Board_tile(True)
        self.black_tile = Board_tile(False)

        # TODO:
        # should probably define board atribute 'field' so we could call something like 'board.8a'
        # then every pawn could be unique (palced on a given field which could be changed)


        # Perhapse this part can be refactorized:
        #################################################################################
        # in a similar fashion: (if (orgn_field_tup[0] + orgn_field_tup[1]) % 2 == 0:)
        # or:
        # ??? grid = np.empty((8, 8), dtype='<U1') ???
        # ??? grid[:] = np.where((np.indices(grid.shape).sum(axis=0) % 2 == 0), 'W', 'B') ???


        # start with all tiles white
        self.board = np.full((8, 8), self.white_tile, dtype = 'O')

        # add black tiles p.1
        self.board[::2, 1::2] = self.black_tile  
        # Setting alternate rows starting from the first row with alternate columns to 

        # add black tiles p.2
        self.board[1::2, ::2] = self.black_tile
        # Setting alternate rows starting from the second row with alternate columns to 1


        #################################################################################



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

    def field_conv(self, fld_address: str) -> Tuple[int, int]:
        """convert field notation (e.g. 8a) to numpy co-ordinates (0, 0)"""

        number, letter = fld_address

        return (8 - int(number), ord(letter) - 97)

    def move(self, move_intr: str) -> None:
        """If the move is vaild moves a given piece on the board
        
        something like this:
        I. 7a>6a (move fig. from field 7a to 6a)
        II. alternatively or perhapes also use simplyfiy chess nontation:
            see: https://www.chess.com/terms/chess-notation"""
        


        # TODO:
        # II. approach 'N3d2' notation (based on standard chess notation but simplify)
        # how to valide the moves instruction to include both types of notatnions?




        #----------------------------------------
        # I. approach 7a>6a notation (move fig. from field 7a to 6a):

        # TODO:
        # check if move istruction is valid (is there any figure on the origin field)
        # check posible moves (how to cross check it with Piece Class?)
        # check if move will create a check on our side (e.g. will expose the king from some angle)


        
        # CHECK what kind of piece object is (is it a tile or rather doas it have 'piece_type' attribute (if not throw an error)
        # CHECK POSSIBLE MOVE 
        # CHECK if given move_inst is in POSSSIBLE MOVES
        # Externalize all this checks form this method (do not do it here)
        # Use method of a given piece which is standing on that field what possbile moves it have







        orgn_field_str, trgt_field_str = move_intr.split('>')
        # split for two addresses

        orgn_field_tup = self.field_conv(orgn_field_str)
        # convert to numpy address tuples

        trgt_field_tup = self.field_conv(trgt_field_str)
        # convert to numpy address tuples

        ####################################################
        # piece_to_move = self.board[orgn_field_tup]
        ####################################################

        if isinstance(self.board[orgn_field_tup], Piece):
            # check if what you have pointed is not an empty field (belongs to the Piece class)
            print("Do the code")
        else:
            raise Exception("You have pointed an empty field as a start!")
            # player has pointed an empty field as a starting point of a move

        
        


        # TODO:
        # check if the move is in a range of a possible moves:
        # piece_to_move.check_move(orgn_field_tup, trgt_field_tup)









        # do the move:
        self.board[trgt_field_tup] = self.board[orgn_field_tup]
        # copy the fig from beginig field to the target field 

        # put original tile to empty place:
        if (orgn_field_tup[0] + orgn_field_tup[1]) % 2 == 0:
        # determin whether tile should be black of white

            self.board[orgn_field_tup] = self.white_tile
            # replace a given piece back with the original tile (white)

        else:
            self.board[orgn_field_tup] = self.black_tile
            # replace a given piece back with the original tile (black)

        self.display_board()

        return None


    def display_board(self, reverse: bool = False) -> None:
        # reverse to be impletemnte later (to reverse board for the second player)

        print('\n' + ' ' * 6 + '-' * 30)

        for idx, row in enumerate(self.board):
            print(8 - idx, ' ' , row)

        print(' ' * 6 + '-' * 30)
        print(' ' * 6 + 'a   b   c   d   e   f   g   h \n')

        return None

    def board_snapshot(self):
        # generate simplify version of a board as a np.array 
        # but only with chars represeinting pieces not actual obejcts.
        pass


#######################################################################################################################
if __name__ == "__main__":

    g1 = Game()

    g1.display_board()

    g1.move('2d>3d')
    g1.move('3d>4d')
    g1.move('4d>5d')

