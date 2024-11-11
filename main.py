# CHESS ENGINE
# v.1.0.3


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
    KING = 'K'
    QUEEN = 'Q'
    TOWER = 'T'
    BISHOP = 'B'
    KNIGHT = 'N'
    PAWN = 'i'

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
# TODO: extract all pieces and related classes and save them as a separate module

class Piece:

    # tuple/vector move notation for pieces:
    
    # (-1,-1)   (-1,0)    (-1,1) 
    #              ^
    #              |
    # (-1,0)  <—  0,0   —> (0,1)
    #              |
    #              ⌄
    # (1,-1)     (1,0)     (1,1) 


    # dictionary of all possible pieces KEY is a tuple (piece color, piece type):
    all_icons_dict = {(Piece_Col.BLACK.value, Piece_Type.KING.value): Piece_Icon.BLACK_KING.value,
                    (Piece_Col.BLACK.value, Piece_Type.QUEEN.value): Piece_Icon.BLACK_QUEEN.value,
                    (Piece_Col.BLACK.value, Piece_Type.TOWER.value): Piece_Icon.BLACK_TOWER.value,
                    (Piece_Col.BLACK.value, Piece_Type.BISHOP.value): Piece_Icon.BLACK_BISHOP.value,
                    (Piece_Col.BLACK.value, Piece_Type.KNIGHT.value): Piece_Icon.BLACK_KNIGHT.value,
                    (Piece_Col.BLACK.value, Piece_Type.PAWN.value): Piece_Icon.BLACK_PAWN.value,
                    (Piece_Col.WHITE.value, Piece_Type.KING.value): Piece_Icon.WHITE_KING.value,
                    (Piece_Col.WHITE.value, Piece_Type.QUEEN.value): Piece_Icon.WHITE_QUEEN.value,
                    (Piece_Col.WHITE.value, Piece_Type.TOWER.value): Piece_Icon.WHITE_TOWER.value,
                    (Piece_Col.WHITE.value, Piece_Type.BISHOP.value): Piece_Icon.WHITE_BISHOP.value,
                    (Piece_Col.WHITE.value, Piece_Type.KNIGHT.value): Piece_Icon.WHITE_KNIGHT.value,
                    (Piece_Col.WHITE.value, Piece_Type.PAWN.value): Piece_Icon.WHITE_PAWN.value}

    # when created piece only requires color and its location
    def __init__(self, color: Piece_Col, field_tup: Tuple[int, int]) -> None:
        
        self.color = color

        self.field_tup = field_tup
    
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

class Pawn(Piece):

    # PAWN MOVE SCHEME:
    # if black pawn can only go down (+1 row on the numpy array), white on the other hand can go only upwad -1 )
    # if board row == 1 or row == 6 you can move 1 or 2 field forward
    # otherwise only one step ahead
    # (En passant to be implement later)

    def __init__(self, color: Piece_Col, field_tup: Tuple[int, int]):

        super().__init__(color, field_tup)
        
        self.piece_type = Piece_Type.PAWN.value
        # assign color to the pawn

        self.icon = self.all_icons_dict[(self.color, self.piece_type)]
        # asign icon to the pawn base on the color



    def check_move(self, orgn_field_tup: Tuple[int, int], 
                       trgt_field_tup: Tuple[int, int]) -> bool:
        
        """check if a given pawn standing on the orgn_field_tup can move to the trgt_field_tup
            (both: orgn_field_tup trgt_field_tup are numpy array co-ordinates e.g. (0, 0 ))
            board_snapshot provide simplify information what is the situation on the board 
            (later optionaly check all possible moves for that piece)"""
        
        is_possible = None

        return is_possible

class Knight(Piece):

    def __init__(self, color: Piece_Col, field_tup: tuple):

        super().__init__(color, field_tup)
        
        self.piece_type = Piece_Type.KNIGHT.value
        self.icon = self.all_icons_dict[(self.color, self.piece_type)]

class Bishop(Piece):
    def __init__(self, color: Piece_Col, field_tup: tuple):

        super().__init__(color, field_tup)
        
        self.piece_type = Piece_Type.BISHOP.value
        self.icon = self.all_icons_dict[(self.color, self.piece_type)]

class Tower(Piece):
    def __init__(self, color: Piece_Col, field_tup: Tuple[int, int]):

        super().__init__(color, field_tup)
        
        self.piece_type: Piece_Col = Piece_Type.TOWER.value
        self.icon: Piece_Icon = self.all_icons_dict[(self.color, self.piece_type)]

    #TODO: IN PROGRESS
    def check_move_rng(self, board_snap: np.array) -> list:
        """Check all theoretically possible moves for this piece - from its starting filed,
        like it would be on an empty board"""
        
        print(self.field_tup)

        moves_rng: list = []

        row_int: int = self.field_tup[0]
        col_int: int = self.field_tup[1]
        

        # vertical:
        for j in range(8):
            if j != row_int:
                moves_rng.append((j, col_int))

        # horizontal:
        for j in range(8):
            if j != col_int:
                moves_rng.append((row_int, j))

        
        print(moves_rng)
        print()
        print(board_snap)
        return None


class Queen(Piece):
    # inherents moves from Bishop and Tower(good to practice multiple inherentance)
    def __init__(self, color: Piece_Col, field_tup: tuple):

        super().__init__(color, field_tup)
        
        self.piece_type = Piece_Type.QUEEN.value
        self.icon = self.all_icons_dict[(self.color, self.piece_type)]

class King(Queen):
    # copy moves from Queen but limit it by one
    def __init__(self, color: Piece_Col, field_tup: tuple):

        super().__init__(color, field_tup)
        
        self.piece_type = Piece_Type.KING.value
        self.icon = self.all_icons_dict[(self.color, self.piece_type)]

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




        # Perhapse this part can be refactorized:
        #################################################################################
        # in a similar fashion: (if (orgn_field_tup[0] + orgn_field_tup[1]) % 2 == 0:)
        # or:
        # ??? grid = np.empty((8, 8), dtype='<U1') ???
        # ??? grid[:] = np.where((np.indices(grid.shape).sum(axis=0) % 2 == 0), 'W', 'B') ???
        #################################################################################

        # start with all tiles white
        self.board = np.full((8, 8), self.white_tile, dtype = 'O')

        # add black tiles p.1
        self.board[::2, 1::2] = self.black_tile  
        # Setting alternate rows starting from the first row with alternate columns to 

        # add black tiles p.2
        self.board[1::2, ::2] = self.black_tile
        # Setting alternate rows starting from the second row with alternate columns to 1


        ######################################################################################################################################
        # PLACE PIECES ON THE BOARD:

        # for each field:
        for i in range(64):
            
            if i < 32:
                chosen_color = Piece_Col.BLACK.value
                # start with black pieces (from the top of the board)
            else:    
                chosen_color = Piece_Col.WHITE.value
                # white for all other

            x = i // 8
            # floor division converts counter to a specific row number
            
            y = i % 8
            # modulo converts counter to a specific column number

            cord_tup = (x, y)
            # return proper numpy coordinates

            # place pawns:
            if i in range(8, 16) or i in range(48, 56):
                self.board[cord_tup] = Pawn(color = chosen_color, field_tup = cord_tup)
            
            # place towers:
            if i in (0, 7, 56, 63):
                self.board[cord_tup] = Tower(color = chosen_color, field_tup = cord_tup)
            
            # place knights:
            if i in (1, 6, 57, 62):
                self.board[cord_tup] = Knight(color = chosen_color, field_tup = cord_tup)
            
            # place bishops:
            if i in (2, 5, 58, 61):
                self.board[cord_tup] = Bishop(color = chosen_color, field_tup = cord_tup)
            
            # place queens:
            if i in (3, 59):
                self.board[cord_tup] = Queen(color = chosen_color, field_tup = cord_tup)
            
            # place kings:    
            if i in (4, 60):
                self.board[cord_tup] = King(color = chosen_color, field_tup = cord_tup)


######################################################################################################################################



    def field_conv(self, fld_address: str) -> Tuple[int, int]:
        """convert field notation given by a player (e.g. 8a) to numpy co-ordinates (0, 0)"""

        number, letter = fld_address

        return (8 - int(number), ord(letter) - 97)

    def move(self, move_intr: str) -> None:
        """If the move is vaild moves a given piece on the board

        Two possible approaches:

        I. 7a>6a (move fig. from field 7a to 6a)
        II. alternatively or perhapes additionally use simplyfiy chess nontation 'N3d2':
            see: https://www.chess.com/terms/chess-notation"""
        
        # TODO:
        #----------------------------------------
        # I. approach:




        orgn_field_str, trgt_field_str = move_intr.split('>')
        # split for two addresses
        # pehapse overload of '__gt__' dunder method could be applied (later)

        orgn_field_tup = self.field_conv(orgn_field_str)
        # convert to numpy address tuples

        trgt_field_tup = self.field_conv(trgt_field_str)
        # convert to numpy address tuples

        if isinstance(self.board[orgn_field_tup], Piece):
            # check if what you have pointed is not an empty field (belongs to the Piece class)
            print("Do the code")
        else:
            raise Exception("You have pointed an empty field as a start!")
            # player has pointed an empty field as a starting point of a move

        board_info = self.board_snapshot()
        # get board info 

        self.board[orgn_field_tup].check_move_rng(board_info)
        # pass it to the check_move_rng() method

        # do the move:
        self.board[trgt_field_tup] = self.board[orgn_field_tup]
        # copy the fig from beginig field to the target field 

        self.board[trgt_field_tup].field_tup = trgt_field_tup
        # update the address of the moved piece
        
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

    def board_snapshot(self) -> np.array:
        """generate simplify version of a board as a np.array 
        but it only contains chars represeinting pieces not actual obejcts"""

        # create empty numpy array (data type Unicode with 1 sign)
        brd_snap = np.full((8,8), '', dtype = 'U2')
        
        for i in range(64):
        # for every field
            
            x = i // 8
            # floor division converts counter to a specific row number

            y = i % 8
            # modulo converts counter to a specific column number
            
            cord_tup = (x, y)
            # return proper numpy coordinates

            current_piece = self.board[cord_tup]
            # get piece from a current field

            if isinstance(current_piece, Piece):
                # if given obj is a piece

                brd_snap[cord_tup] = f'{current_piece.piece_type}{current_piece.color}'
                # get its 'piece_type' and color attribute

        return brd_snap


#######################################################################################################################
if __name__ == "__main__":

    g1 = Game()
    g1.display_board()

    g1.move('1a>5d')
    g1.move('5d>6d')
